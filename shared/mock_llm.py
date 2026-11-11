"""MockLLM: a deterministic, scripted language model for teaching.

MockLLM doesn't understand language. It returns the replies you script, so lessons can show
how prompts, tool calls, agent loops and RAG pipelines *flow*, with output that is identical on
every run and needs no network or account.

Three ways to script it, checked in this order on every call:
  1. script  -- a queue of replies, returned one per call, in order.
  2. rules   -- (pattern, reply) pairs. The first regular expression that matches the latest
                message's text wins.
  3. default -- the fallback reply. Set default=None to raise an error instead, which is handy
                in tests.

A reply can be a string, a Reply (text and/or tool calls), or a function that receives the
messages and tools and returns either one.

MockLLM also behaves like a real model in the ways that matter for teaching:
  * it refuses to "call" a tool it wasn't offered, or to pass arguments that break the schema,
  * it honours max_tokens (finish_reason="length") and stop sequences,
  * it reports token usage (approximate, see llm_interface.count_tokens),
  * it records every call in `.calls`, so you can inspect exactly what the model was sent.
temperature and seed are accepted and ignored: MockLLM is always deterministic.

Run:  python mock_llm.py

Expected output:
    -- step 1: model asks for a tool
    finish_reason: tool_calls
    tool call: multiply {'a': 6, 'b': 7}
    -- step 2: we run the tool and send back the result
    finish_reason: stop
    answer: 6 times 7 is 42.
    -- rules and default
    Hello! How can I help?
    Sorry, I can only do arithmetic.
    -- limits
    max_tokens=3 -> 'one two three' (length)
    calls recorded: 5, total tokens used: 66
"""

from __future__ import annotations

import re
from collections import deque
from dataclasses import dataclass, field
from typing import Any, Callable, Sequence, Union

if __package__:
    from .llm_interface import (
        GenerationResult,
        Message,
        ToolCall,
        ToolSpec,
        Usage,
        check_arguments,
        count_tokens,
    )
else:  # running this file directly: python mock_llm.py
    from llm_interface import (  # type: ignore[no-redef]
        GenerationResult,
        Message,
        ToolCall,
        ToolSpec,
        Usage,
        check_arguments,
        count_tokens,
    )


@dataclass(frozen=True)
class Reply:
    """A scripted assistant turn: text, tool calls, or both.

    Tool calls are given as (name, arguments) pairs. MockLLM assigns their ids.
    """

    text: str = ""
    tool_calls: tuple[tuple[str, dict[str, Any]], ...] = ()

    @staticmethod
    def call(name: str, **arguments: Any) -> "Reply":
        """Shorthand for a reply that asks for exactly one tool call."""
        return Reply(tool_calls=((name, arguments),))


Responder = Callable[[Sequence[Message], Sequence[ToolSpec]], Union[str, Reply]]
ReplyLike = Union[str, Reply, Responder]


@dataclass(frozen=True)
class Rule:
    """Reply with `reply` when `pattern` (a regular expression) matches the latest message."""

    pattern: str
    reply: ReplyLike

    def matches(self, text: str) -> bool:
        return re.search(self.pattern, text, flags=re.IGNORECASE) is not None


@dataclass
class CallRecord:
    """Everything one generate() call received and returned."""

    messages: tuple[Message, ...]
    tools: tuple[ToolSpec, ...]
    result: GenerationResult


class ScriptExhausted(RuntimeError):
    """Raised when no script item, rule or default applies to a call."""


@dataclass
class MockLLM:
    script: Sequence[ReplyLike] = ()
    rules: Sequence[Rule] = ()
    default: ReplyLike | None = "I don't know."
    calls: list[CallRecord] = field(default_factory=list, init=False)

    def __post_init__(self) -> None:
        self._queue: deque[ReplyLike] = deque(self.script)
        self._next_call_id = 1

    def generate(
        self,
        messages: Sequence[Message],
        *,
        tools: Sequence[ToolSpec] | None = None,
        max_tokens: int = 256,
        temperature: float = 0.0,
        stop: Sequence[str] | None = None,
        seed: int | None = None,
    ) -> GenerationResult:
        if not messages:
            raise ValueError("generate() needs at least one message")
        tools = tuple(tools or ())
        reply = self._resolve(self._pick(messages), messages, tools)

        tool_calls = self._make_tool_calls(reply, tools)
        text = reply.text
        finish: str = "tool_calls" if tool_calls else "stop"

        for s in stop or ():
            if s and s in text:
                text = text[: text.index(s)]
        if count_tokens(text) > max_tokens:
            text = _truncate(text, max_tokens)
            finish = "length"

        usage = Usage(
            input_tokens=sum(count_tokens(m.content) for m in messages),
            output_tokens=count_tokens(text) + sum(
                count_tokens(f"{c.name} {c.arguments}") for c in tool_calls
            ),
        )
        result = GenerationResult(text=text, finish_reason=finish, usage=usage,  # type: ignore[arg-type]
                                  tool_calls=tool_calls)
        self.calls.append(CallRecord(tuple(messages), tools, result))
        return result

    def reset(self) -> None:
        """Restart the script and forget recorded calls."""
        self._queue = deque(self.script)
        self._next_call_id = 1
        self.calls.clear()

    # --- internals ------------------------------------------------------------------------

    def _pick(self, messages: Sequence[Message]) -> ReplyLike:
        if self._queue:
            return self._queue.popleft()
        latest = messages[-1].content
        for rule in self.rules:
            if rule.matches(latest):
                return rule.reply
        if self.default is None:
            raise ScriptExhausted(f"no scripted reply for message: {latest!r}")
        return self.default

    @staticmethod
    def _resolve(item: ReplyLike, messages: Sequence[Message], tools: Sequence[ToolSpec]) -> Reply:
        if callable(item) and not isinstance(item, Reply):
            item = item(messages, tools)
        if isinstance(item, str):
            return Reply(text=item)
        if isinstance(item, Reply):
            return item
        raise TypeError(f"a scripted reply must be str, Reply or callable, not {type(item).__name__}")

    def _make_tool_calls(self, reply: Reply, tools: Sequence[ToolSpec]) -> tuple[ToolCall, ...]:
        offered = {t.name: t for t in tools}
        calls = []
        for name, arguments in reply.tool_calls:
            if name not in offered:
                raise ValueError(
                    f"script asks for tool {name!r}, but this call only offered {sorted(offered)}"
                )
            problems = check_arguments(offered[name], arguments)
            if problems:
                raise ValueError(f"scripted arguments for {name!r} break its schema: {problems}")
            calls.append(ToolCall(id=f"call_{self._next_call_id}", name=name, arguments=dict(arguments)))
            self._next_call_id += 1
        return tuple(calls)


def _truncate(text: str, max_tokens: int) -> str:
    """Cut text after `max_tokens` approximate tokens."""
    for end in range(len(text) + 1):
        if count_tokens(text[:end]) > max_tokens:
            return text[: end - 1].rstrip()
    return text


if __name__ == "__main__":
    if __package__:
        from .llm_interface import system, tool_result, user
    else:
        from llm_interface import system, tool_result, user  # type: ignore[no-redef]

    multiply = ToolSpec(
        name="multiply",
        description="Multiply two numbers.",
        parameters={
            "type": "object",
            "properties": {"a": {"type": "number"}, "b": {"type": "number"}},
            "required": ["a", "b"],
        },
    )

    # A two-step tool-calling exchange, fully scripted.
    model = MockLLM(script=[Reply.call("multiply", a=6, b=7), "6 times 7 is 42."])
    conversation = [system("You are a careful calculator."), user("What is 6 times 7?")]

    print("-- step 1: model asks for a tool")
    first = model.generate(conversation, tools=[multiply])
    print("finish_reason:", first.finish_reason)
    call = first.tool_calls[0]
    print("tool call:", call.name, call.arguments)

    print("-- step 2: we run the tool and send back the result")
    conversation += [first.to_message(), tool_result(call, str(call.arguments["a"] * call.arguments["b"]))]
    second = model.generate(conversation, tools=[multiply])
    print("finish_reason:", second.finish_reason)
    print("answer:", second.text)

    print("-- rules and default")
    model2 = MockLLM(rules=[Rule(r"\b(hi|hello)\b", "Hello! How can I help?")],
                     default="Sorry, I can only do arithmetic.")
    print(model2.generate([user("Hi there")]).text)
    print(model2.generate([user("Write me a poem")]).text)

    print("-- limits")
    model3 = MockLLM(default="one two three four five")
    short = model3.generate([user("Count")], max_tokens=3)
    print(f"max_tokens=3 -> {short.text!r} ({short.finish_reason})")

    used = sum(r.result.usage.total_tokens for m in (model, model2, model3) for r in m.calls)
    print(f"calls recorded: {len(model.calls) + len(model2.calls) + len(model3.calls)}, total tokens used: {used}")

"""A minimal, model-agnostic interface for language models.

Every lesson that needs "a language model" codes against this file, never against a specific
provider. Anything with a `generate()` method of the right shape is a `LanguageModel`:
  * MockLLM (shared/mock_llm.py): scripted, deterministic responses for teaching control flow.
  * TinyLM (added in L2-15): the small transformer you build yourself.
  * Your own adapter for a real model (see shared/README.md). The repo never ships one.

The design follows patterns common across the industry, without copying any one product:
  * A conversation is a list of messages. Each has a role: system, user, assistant or tool.
  * Calls are stateless. You send the whole conversation every time.
  * A model may answer with text, or with requests to call tools you described.

Run:  python llm_interface.py

Expected output:
    system    : You are a helpful assistant.
    user      : What is 6 times 7?
    assistant : (tool call) multiply {'a': 6, 'b': 7}
    tool      : 42
    assistant : 6 times 7 is 42.
    argument errors for {'a': 'six'}: ["'a' must be number", "missing required argument 'b'"]
    approximate tokens in 'What is 6 times 7?': 6
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal, Protocol, Sequence, runtime_checkable

Role = Literal["system", "user", "assistant", "tool"]
FinishReason = Literal["stop", "length", "tool_calls"]
ROLES: tuple[str, ...] = ("system", "user", "assistant", "tool")


@dataclass(frozen=True)
class ToolSpec:
    """A tool the model may ask to call.

    `parameters` describes the arguments with a small subset of JSON Schema (an open
    specification): {"type": "object", "properties": {...}, "required": [...]}.
    """

    name: str
    description: str
    parameters: dict[str, Any] = field(
        default_factory=lambda: {"type": "object", "properties": {}, "required": []}
    )


@dataclass(frozen=True)
class ToolCall:
    """The model's request to run one tool with some arguments."""

    id: str
    name: str
    arguments: dict[str, Any]


@dataclass(frozen=True)
class Message:
    """One turn in a conversation."""

    role: Role
    content: str = ""
    tool_calls: tuple[ToolCall, ...] = ()
    tool_call_id: str | None = None  # set on role="tool" messages: which call this answers

    def __post_init__(self) -> None:
        if self.role not in ROLES:
            raise ValueError(f"unknown role {self.role!r}; expected one of {ROLES}")
        if self.role == "tool" and not self.tool_call_id:
            raise ValueError("a tool message must say which call it answers (tool_call_id)")
        if self.tool_calls and self.role != "assistant":
            raise ValueError("only assistant messages can contain tool calls")


@dataclass(frozen=True)
class Usage:
    """How many tokens went in and came out. Costs and limits are counted in tokens."""

    input_tokens: int
    output_tokens: int

    @property
    def total_tokens(self) -> int:
        return self.input_tokens + self.output_tokens


@dataclass(frozen=True)
class GenerationResult:
    """What a model returns from one call."""

    text: str
    finish_reason: FinishReason  # "stop", "length" (hit max_tokens) or "tool_calls"
    usage: Usage
    tool_calls: tuple[ToolCall, ...] = ()

    def to_message(self) -> Message:
        """The assistant message to append to the conversation before the next call."""
        return Message("assistant", self.text, tool_calls=self.tool_calls)


@runtime_checkable
class LanguageModel(Protocol):
    """Anything that can continue a conversation."""

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
        """Return the next assistant turn for `messages`.

        tools        -- tools the model may ask to call this turn
        max_tokens   -- upper limit on generated tokens; hitting it sets finish_reason="length"
        temperature  -- randomness of sampling; 0 means always pick the most likely token
        stop         -- strings that end generation early
        seed         -- makes sampling repeatable, where the model supports it
        """
        ...


# --- Small helpers ------------------------------------------------------------------------


def system(content: str) -> Message:
    return Message("system", content)


def user(content: str) -> Message:
    return Message("user", content)


def assistant(content: str) -> Message:
    return Message("assistant", content)


def tool_result(call: ToolCall, content: str) -> Message:
    """The message that carries a tool's output back to the model."""
    return Message("tool", content, tool_call_id=call.id)


def count_tokens(text: str) -> int:
    """A rough token count: words and punctuation marks.

    Real models split text with a learned tokenizer (see L2-01), so their counts differ. This
    approximation is only for teaching budgets and usage accounting with MockLLM.
    """
    count = 0
    word = False
    for ch in text:
        if ch.isalnum() or ch in "_'":
            if not word:
                count += 1
                word = True
        else:
            word = False
            if not ch.isspace():
                count += 1
    return count


_JSON_TYPES: dict[str, tuple[type, ...]] = {
    "string": (str,),
    "number": (int, float),
    "integer": (int,),
    "boolean": (bool,),
    "array": (list, tuple),
    "object": (dict,),
}


def check_arguments(spec: ToolSpec, arguments: dict[str, Any]) -> list[str]:
    """Check tool-call arguments against the tool's schema. Returns a list of problems.

    Supports a small subset of JSON Schema: object properties with a "type", "enum" and
    "required". That is enough to teach validation; production systems use a full validator.
    """
    errors: list[str] = []
    props: dict[str, Any] = spec.parameters.get("properties", {})
    for name, value in arguments.items():
        if name not in props:
            errors.append(f"unexpected argument {name!r}")
            continue
        expected = props[name].get("type")
        if expected:
            ok_types = _JSON_TYPES.get(expected, (object,))
            # bool is a subclass of int in Python, but not a number in JSON Schema.
            if isinstance(value, bool) and expected in ("number", "integer"):
                errors.append(f"{name!r} must be {expected}")
            elif not isinstance(value, ok_types):
                errors.append(f"{name!r} must be {expected}")
        allowed = props[name].get("enum")
        if allowed is not None and value not in allowed:
            errors.append(f"{name!r} must be one of {allowed}")
    for name in spec.parameters.get("required", []):
        if name not in arguments:
            errors.append(f"missing required argument {name!r}")
    return errors


def _show(message: Message) -> str:
    if message.tool_calls:
        calls = ", ".join(f"{c.name} {c.arguments}" for c in message.tool_calls)
        return f"{message.role:<10}: (tool call) {calls}"
    return f"{message.role:<10}: {message.content}"


if __name__ == "__main__":
    multiply = ToolSpec(
        name="multiply",
        description="Multiply two numbers.",
        parameters={
            "type": "object",
            "properties": {"a": {"type": "number"}, "b": {"type": "number"}},
            "required": ["a", "b"],
        },
    )
    call = ToolCall(id="call_1", name="multiply", arguments={"a": 6, "b": 7})
    conversation = [
        system("You are a helpful assistant."),
        user("What is 6 times 7?"),
        Message("assistant", tool_calls=(call,)),
        tool_result(call, "42"),
        assistant("6 times 7 is 42."),
    ]
    for m in conversation:
        print(_show(m))
    print("argument errors for {'a': 'six'}:", check_arguments(multiply, {"a": "six"}))
    print("approximate tokens in 'What is 6 times 7?':", count_tokens("What is 6 times 7?"))

# Shared Code: One Interface for Every Language Model

Every lesson that needs "a language model" uses the small interface in this folder, never a
specific provider. That keeps the catalog offline, free, deterministic and vendor-neutral, and
it teaches the most durable lesson of all: **your application should depend on an interface,
not on a model.**

| File | What it is |
|---|---|
| [`llm_interface.py`](llm_interface.py) | The interface: `Message`, `ToolSpec`, `ToolCall`, `GenerationResult`, `Usage` and the `LanguageModel` protocol, plus helpers |
| [`mock_llm.py`](mock_llm.py) | `MockLLM`, a scripted, deterministic model for teaching control flow |
| `tiny_lm.py` *(planned, L2-15)* | `TinyLM`, the character-level transformer you build in Level 2, behind the same interface |

## The interface in one minute

A conversation is a list of messages. Each message has a **role**:

| Role | Who writes it | Example |
|---|---|---|
| `system` | You, the developer | "You are a careful calculator." |
| `user` | The person using your app | "What is 6 times 7?" |
| `assistant` | The model | "6 times 7 is 42." or a request to call a tool |
| `tool` | Your code, after running a tool | "42" |

You call `generate()` with the **whole** conversation every time. Models don't remember earlier
calls; your application holds the state.

```python
result = model.generate(
    messages,                 # the conversation so far
    tools=[multiply],         # tools the model may ask to call (optional)
    max_tokens=256,           # upper limit on output length
    temperature=0.0,          # 0 = always pick the most likely continuation
    stop=None,                # strings that end generation early
    seed=None,                # repeatable sampling, where supported
)
result.text            # the answer text
result.tool_calls      # tool requests, if any
result.finish_reason   # "stop", "length" or "tool_calls"
result.usage           # input and output token counts
```

Anything with this `generate()` method satisfies the `LanguageModel` protocol, whatever is behind it.

## Using MockLLM

```python
from shared.llm_interface import ToolSpec, user
from shared.mock_llm import MockLLM, Reply, Rule

# A queue of replies, returned in order:
model = MockLLM(script=[Reply.call("multiply", a=6, b=7), "6 times 7 is 42."])

# Or pattern-based rules, with a fallback:
model = MockLLM(rules=[Rule(r"\bhello\b", "Hi!")], default="I don't know.")
```

MockLLM checks its own script the way a careful reviewer would. It raises an error if a scripted
tool call names a tool that wasn't offered, or if its arguments break the tool's schema. Every
call is recorded in `model.calls` so lessons can show exactly what was sent. Run
`python shared/mock_llm.py` for a full tool-calling example.

## Writing your own adapter

This repository **never ships an adapter for a real model provider**. Products and their APIs
change faster than the ideas this catalog teaches, and a vendor adapter would tie the lessons to
one company. If you want to try the lessons with a real model, write a small adapter yourself.
It's a good exercise in its own right.

An adapter is a class with a `generate()` method that translates in both directions:

```python
from shared.llm_interface import GenerationResult, Message, ToolSpec, Usage


class MyModelAdapter:
    """Connects the catalog's interface to a model of your choice."""

    def generate(self, messages, *, tools=None, max_tokens=256,
                 temperature=0.0, stop=None, seed=None) -> GenerationResult:
        # 1. Translate `messages` into the format your model expects (roles, tool results).
        # 2. Translate `tools` into its tool-description format (most accept JSON Schema).
        # 3. Call the model, with a timeout.
        # 4. Translate the response back: text, tool calls (with ids), finish reason, usage.
        raise NotImplementedError("Write this for the model you want to use.")
```

Things to get right:

- **Map finish reasons** onto `"stop"`, `"length"` and `"tool_calls"`.
- **Keep tool-call ids.** Each `tool` message must reference the id of the call it answers.
- **Count usage** from what the model reports, not from `count_tokens()`, which is only an
  approximation for teaching.
- **Handle failure:** timeouts, rate limits and malformed tool calls. Level 5 covers retries and fallbacks.
- **Keep secrets out of code.** Read credentials from an environment variable or a secrets
  store. Never commit them. Keep your adapter outside this repository, or in a git-ignored file.
- **Test it with the lessons' expected outputs.** Real models won't match MockLLM's scripted
  output word for word, so judge the behaviour, not the exact text.

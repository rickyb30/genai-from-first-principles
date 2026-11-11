"""Solution (L0-02): six more systems on the nested map.

Notes on the trickier ones:
  * Thermostat: a fixed threshold rule. Most people wouldn't call that AI.
  * Route planner: searching a map is a classic AI technique, but nothing is learned.
  * Rule-based chatbot: it produces text, but from hand-written templates. It's AI in the
    older, symbolic sense, and it's not generative AI, because nothing was learned from data.
  * House-price line: fitting a line to data IS machine learning, even if it's simple.

Run:  python place_these.py

Expected output:
    Thermostat          ->  Not AI: conventional software
    Route planner       ->  AI, but not machine learning
    Speech-to-text      ->  Deep learning, but not generative
    Music generator     ->  Generative AI (deep learning that creates content)
    House-price line    ->  Machine learning, but not deep learning
    Rule-based chatbot  ->  AI, but not machine learning
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class System:
    name: str
    does_ai_task: bool
    learns_from_data: bool
    deep_network: bool
    generates: bool


def place(s: System) -> str:
    if not s.does_ai_task:
        return "Not AI: conventional software"
    if not s.learns_from_data:
        return "AI, but not machine learning"
    if not s.deep_network:
        if s.generates:
            return "Machine learning: a simple generative model (not deep learning)"
        return "Machine learning, but not deep learning"
    if s.generates:
        return "Generative AI (deep learning that creates content)"
    return "Deep learning, but not generative"


SYSTEMS = [
    System("Thermostat", False, False, False, False),
    System("Route planner", True, False, False, False),
    System("Speech-to-text", True, True, True, False),
    System("Music generator", True, True, True, True),
    System("House-price line", True, True, False, False),
    System("Rule-based chatbot", True, False, False, True),
]

if __name__ == "__main__":
    width = max(len(s.name) for s in SYSTEMS)
    for s in SYSTEMS:
        print(f"{s.name:<{width}}  ->  {place(s)}")

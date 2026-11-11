"""Place systems on the nested map of AI, machine learning, deep learning and generative AI.

Each system is described by four yes/no questions. The function `place` walks inward
through the map, one question at a time, and stops at the innermost circle that fits.

Run:  python where_does_it_fit.py

Expected output:
    Tax calculator applying fixed formulas                   ->  Not AI: conventional software
    Chess program searching moves with hand-written scoring  ->  AI, but not machine learning
    Spam filter that counts words in labelled emails         ->  Machine learning, but not deep learning
    Word-pair text generator (like L0-01's)                  ->  Machine learning: a simple generative model (not deep learning)
    Photo app that recognizes faces with a deep network      ->  Deep learning, but not generative
    Chat assistant built on a large language model           ->  Generative AI (deep learning that creates content)
    Image generator that turns a description into a picture  ->  Generative AI (deep learning that creates content)
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class System:
    name: str
    does_ai_task: bool      # perceives, reasons, plans, decides or creates in a way we'd call intelligent
    learns_from_data: bool  # its behaviour comes from examples, not only from hand-written rules
    deep_network: bool      # it uses a neural network with many layers
    generates: bool         # its main output is new content: text, images, audio, code


def place(s: System) -> str:
    """Walk inward through the nested map and return the innermost region that fits."""
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
    System("Tax calculator applying fixed formulas", False, False, False, False),
    System("Chess program searching moves with hand-written scoring", True, False, False, False),
    System("Spam filter that counts words in labelled emails", True, True, False, False),
    System("Word-pair text generator (like L0-01's)", True, True, False, True),
    System("Photo app that recognizes faces with a deep network", True, True, True, False),
    System("Chat assistant built on a large language model", True, True, True, True),
    System("Image generator that turns a description into a picture", True, True, True, True),
]


def main() -> None:
    width = max(len(s.name) for s in SYSTEMS)
    for s in SYSTEMS:
        print(f"{s.name:<{width}}  ->  {place(s)}")


if __name__ == "__main__":
    main()

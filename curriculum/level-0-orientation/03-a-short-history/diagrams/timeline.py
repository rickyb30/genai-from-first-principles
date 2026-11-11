"""Draw a simplified timeline of AI: waves of progress and two "AI winters".

Dates of the winters are approximate. Historians draw the boundaries differently.

Run:  python timeline.py

Expected output:
    wrote timeline.png
"""

import sys
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "shared").is_dir())
sys.path.insert(0, str(ROOT))

from shared.diagram_kit import Diagram  # noqa: E402

d = Diagram(title="A simplified timeline of AI", box_size=(3.2, 1.5))

eras = [
    ("birth", "1950s", "The field is born", "test proposals, first programs"),
    ("early", "1956–early 1970s", "Early optimism", "search, logic, first chatbot"),
    ("winter1", "mid-1970s", "First AI winter", "funding cut, hopes deflated"),
    ("expert", "1980s", "Expert systems", "hand-written rules, sold widely"),
    ("winter2", "late 1980s–early 1990s", "Second AI winter", "rule systems prove brittle"),
    ("stats", "1990s–2000s", "Learning from data", "statistical machine learning"),
    ("deep", "2010s", "Deep learning", "big data, fast chips, deep nets"),
    ("gen", "late 2010s–now", "Generative AI", "transformers, large models"),
]
positions = [(0, 2.2), (4.0, 2.2), (8.0, 2.2), (12.0, 2.2), (12.0, 0), (8.0, 0), (4.0, 0), (0, 0)]  # a snake: row 2 runs right to left
for (key, years, title, sub), (x, y) in zip(eras, positions):
    kind = "external" if key.startswith("winter") else ("action" if key == "gen" else "default")
    d.box(key, x, y, f"{years}\n{title}", subtitle=sub, kind=kind, h=1.6)

keys = [e[0] for e in eras]
for a, b in zip(keys, keys[1:]):
    d.arrow(a, b)

print("wrote", d.save(Path(__file__).with_suffix(".png")).name)

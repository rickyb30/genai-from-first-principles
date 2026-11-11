"""Render the catalog's level dependency map as a PNG.

Run:  python level_map.py

Expected output:
    wrote level_map.png
"""

import sys
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "shared").is_dir())
sys.path.insert(0, str(ROOT))

from shared.diagram_kit import Diagram  # noqa: E402

HERE = Path(__file__).parent

d = Diagram(title="How the levels build on each other", box_size=(2.4, 1.35))

core = [
    ("L0", 0.0, "L0 Orientation", "6 lessons · 2.6 h"),
    ("L1", 3.0, "L1 Foundations\nfor Generative AI", "10 lessons · 9.2 h"),
    ("L2", 6.0, "L2 Deep Learning &\nGenerative Models", "15 lessons · 13.8 h"),
    ("L3", 9.0, "L3 Building\nwith LMs", "14 lessons · 12.6 h"),
    ("L4", 12.0, "L4 Agentic\nSystems", "11 lessons · 10.2 h"),
]
for key, x, label, sub in core:
    d.box(key, x, 2.0, label, subtitle=sub, w=2.7 if key in ("L1", "L2") else None)

d.box("L5", 15.0, 3.4, "L5 Production\n/ LLMOps", subtitle="11 lessons · 11 h", kind="action")
d.box("L6", 15.0, 0.6, "L6 Safety, Security\n& Governance", subtitle="13 lessons · 12.2 h",
      kind="risk", w=2.7)
d.box("L7", 18.0, 2.0, "L7 Expert\n& Frontier", subtitle="12 lessons · 12.8 h", kind="data")

for a, b in [("L0", "L1"), ("L1", "L2"), ("L2", "L3"), ("L3", "L4"),
             ("L4", "L5"), ("L4", "L6"), ("L5", "L7"), ("L6", "L7")]:
    d.arrow(a, b)
d.arrow("L3", "L5", curve=-0.35, dashed=True, label="evaluation & RAG")

d.group("Core path — read in order", ["L0", "L1", "L2", "L3", "L4"], kind="default")

print("wrote", d.save(HERE / "level_map.png").name)

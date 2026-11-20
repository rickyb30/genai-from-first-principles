"""Draw generation as repeated sampling: look up a distribution, sample, append, repeat.

Run:  python generation_loop.py

Expected output:
    wrote generation_loop.png
"""

import sys
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "shared").is_dir())
sys.path.insert(0, str(ROOT))

from shared.diagram_kit import Diagram  # noqa: E402

d = Diagram(title="Generation is repeated sampling", box_size=(3.4, 1.3))
d.box("so_far", 0, 2.4, "Sequence so far", subtitle="sunny, sunny", kind="data")
d.box("lookup", 5.2, 2.4, "Get P(next | so far)", subtitle="sunny 0.7 · cloudy 0.2 · rain 0.1")
d.box("sample", 5.2, 0, "Sample one outcome", subtitle="draw u = 0.78 → cloudy", kind="action")
d.box("append", 0, 0, "Append it", subtitle="sunny, sunny, cloudy", kind="data")
d.arrow("so_far", "lookup", label="1")
d.arrow("lookup", "sample", label="2")
d.arrow("sample", "append", label="3")
d.arrow("append", "so_far", label="repeat")
d.note(2.6, -1.35, "A language model runs the same loop, with tokens instead of weather.")

print("wrote", d.save(Path(__file__).with_suffix(".png")).name)

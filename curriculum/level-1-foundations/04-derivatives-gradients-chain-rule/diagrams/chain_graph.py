"""Draw the computational graph of L(w) = (2w - 6)^2, with forward values and backward gradients.

Run:  python chain_graph.py

Expected output:
    wrote chain_graph.png
"""

import sys
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "shared").is_dir())
sys.path.insert(0, str(ROOT))

from shared.diagram_kit import Diagram  # noqa: E402

d = Diagram(title="Forward pass computes values; backward pass multiplies local slopes",
            box_size=(2.6, 1.3))
d.box("w", 0, 2, "w", subtitle="value 1", kind="data")
d.box("u", 4.5, 2, "u = 2w - 6", subtitle="value -4")
d.box("L", 9, 2, "L = u²", subtitle="value 16", kind="action")
d.arrow("w", "u", label="forward")
d.arrow("u", "L", label="forward")

d.box("gw", 0, 0, "dL/dw = -16", subtitle="-8 × 2", kind="data")
d.box("gu", 4.5, 0, "dL/du = -8", subtitle="2u = 2 × (-4)")
d.box("gL", 9, 0, "dL/dL = 1", subtitle="start here", kind="action")
d.arrow("gL", "gu", label="× local slope 2u")
d.arrow("gu", "gw", label="× local slope 2")
d.note(4.5, -1.25, "Backward pass: start at the output with 1, then multiply by each step's "
       "local slope on the way back.")

print("wrote", d.save(Path(__file__).with_suffix(".png")).name)

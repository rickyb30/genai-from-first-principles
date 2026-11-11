"""Draw the six setup steps, from installing Python to checking an example's output.

Run:  python setup_steps.py

Expected output:
    wrote setup_steps.png
"""

import sys
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "shared").is_dir())
sys.path.insert(0, str(ROOT))

from shared.diagram_kit import Diagram  # noqa: E402

d = Diagram(title="From nothing to your first example, in six steps", box_size=(3.3, 1.4))

steps = [
    ("python", 0, 2.4, "1  Install Python", "version 3.11 or newer", "external"),
    ("code", 4.6, 2.4, "2  Get the catalog", "clone or download", "data"),
    ("venv", 9.2, 2.4, "3  Create a\nvirtual environment", "one per project", "default"),
    ("install", 9.2, 0, "4  Install packages", "pinned versions", "default"),
    ("run", 4.6, 0, "5  Run an example", "python file.py", "action"),
    ("compare", 0, 0, "6  Compare output", "with 'Expected output'", "human"),
]
for key, x, y, label, sub, kind in steps:
    d.box(key, x, y, label, subtitle=sub, kind=kind, h=1.5)
for a, b in zip([s[0] for s in steps], [s[0] for s in steps][1:]):
    d.arrow(a, b)

print("wrote", d.save(Path(__file__).with_suffix(".png")).name)

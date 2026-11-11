"""Draw a two-question guide: how much checking does a generated output need?

Run:  python who_checks.py

Expected output:
    wrote who_checks.png
"""

import sys
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "shared").is_dir())
sys.path.insert(0, str(ROOT))

from shared.diagram_kit import Diagram  # noqa: E402

d = Diagram(title="How much checking does a generated output need?", box_size=(3.4, 1.3))

d.box("out", 0, 3.0, "Generated output", kind="action")
d.box("q1", 5.2, 3.0, "Could an error hurt someone,\ncost money or break a rule?")
d.box("review", 11.0, 3.0, "A person reviews it\nbefore it's used", kind="human")
d.box("q2", 5.2, 0.0, "Does it state facts\nsomeone will rely on?")
d.box("check", 11.0, 0.0, "Check the facts\nagainst trusted sources", kind="human")
d.box("use", 5.2, -3.0, "Use it,\nand stay alert", kind="default")

d.arrow("out", "q1")
d.arrow("q1", "review", label="yes")
d.arrow("q1", "q2", label="no")
d.arrow("q2", "check", label="yes")
d.arrow("q2", "use", label="no")

print("wrote", d.save(Path(__file__).with_suffix(".png")).name)

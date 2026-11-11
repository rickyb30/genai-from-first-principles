"""Draw the learning loop the catalog is designed around: read, try, check, review.

Run:  python learning_loop.py

Expected output:
    wrote learning_loop.png
"""

import sys
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "shared").is_dir())
sys.path.insert(0, str(ROOT))

from shared.diagram_kit import Diagram  # noqa: E402

d = Diagram(title="The learning loop behind every lesson", box_size=(3.4, 1.4))

d.box("read", 0, 3.2, "1  Read", subtitle="core idea, then deeper if you want", kind="default")
d.box("try", 7.0, 3.2, "2  Try", subtitle="run the code, do the exercise", kind="action")
d.box("check", 7.0, 0, "3  Check", subtitle="answer the quiz before peeking", kind="human")
d.box("review", 0, 0, "4  Review later", subtitle="flashcards, spaced over days", kind="data")

d.arrow("read", "try")
d.arrow("try", "check")
d.arrow("check", "review")
d.arrow("review", "read", label="next lesson")

print("wrote", d.save(Path(__file__).with_suffix(".png")).name)

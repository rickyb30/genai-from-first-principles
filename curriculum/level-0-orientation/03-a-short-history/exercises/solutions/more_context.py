"""Solution (L0-03): more context on a small text means more copying.

With a long context, most contexts in a 152-word text were seen only once, so there is only
one possible next letter. The generator stops inventing and starts reciting the source.
This is a tiny version of a real issue: models can memorize and repeat parts of their
training data, especially text they saw many times or text that is rare and distinctive.
Level 6 returns to this as a privacy risk.

Run:  python more_context.py

Expected output:
     2 letters of context: brain thas halk a museves a librarket on the rives crosseum
       longest copied run: 10 of 60 characters
     6 letters of context: brindlewick is a small town council meets on the east bank o
       longest copied run: 28 of 60 characters
     8 letters of context: brindlewick is a small town on the east bank of the river as
       longest copied run: 60 of 60 characters
    12 letters of context: brindlewick is a small town on the east bank of the river as
       longest copied run: 60 of 60 characters
"""

import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "code"))
from shannon_approximations import TEXT, clean, letters_order  # noqa: E402


def longest_copied_run(generated: str, source: str) -> int:
    best = 0
    for start in range(len(generated)):
        length = best + 1  # only look for runs longer than the best so far
        while start + length <= len(generated) and generated[start:start + length] in source:
            best = length
            length += 1
    return best


if __name__ == "__main__":
    text = clean(TEXT)
    rng = random.Random(7)
    for context in (2, 6, 8, 12):
        sample = letters_order(text, context, 60, rng)
        print(f"{context:>2} letters of context: {sample}")
        print(f"   longest copied run: {longest_copied_run(sample, text)} of 60 characters")

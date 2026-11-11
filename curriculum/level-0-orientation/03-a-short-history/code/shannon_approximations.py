"""Recreate a 1948 experiment: generating text from statistics alone.

In "A Mathematical Theory of Communication" (1948), Claude Shannon produced a series of
increasingly English-like "approximations" by choosing each letter (or word) at random,
using statistics collected from real text. Each step uses more context: zero letters of
context, then one, then two. This file also goes one step further than his printed examples,
to four letters. Modern language models follow the same basic recipe, predicting
the next piece of text from the text before it, with far more context and far better statistics.

The source text is an original passage about Brindlewick, the fictional town used throughout
this catalog.

Run:  python shannon_approximations.py

Expected output:
    source: 152 words, 777 characters

    letters, all equally likely     : nglbunkzvfhadm uawecjnxxdyiwuubyazbfqr bo omcdkenavuxn qgazi
    letters, by frequency           : no atshhaitesl p  rou  cv seien isc  estnsdcadronsenntarstoo
    letters, 1 letter of context    : balo meun crs mofisicke fo rethocle t wnd thay d fe are o g
    letters, 2 letters of context   : brary closeum in tre is town the rive muses the the of hast
    letters, 4 letters of context   : brindlewick is wound by hand everyone the library open to ca
    words, by frequency             : market museum stops of the on the every in the
    words, 1 word of context        : brindlewick is closed to everyone who arrive by train can walk to
"""

import random
import string
from collections import Counter, defaultdict

TEXT = """
Brindlewick is a small town on the east bank of the river Ashwater. The town has a library,
a market, a ferry and a museum of clocks. The library opens at nine in the morning and closes
at six in the evening. The market opens on Saturday and Sunday, and on market days the main
street is closed to cars. The ferry crosses the river every half hour, and the first ferry
leaves at seven. Visitors who arrive by train can walk to the ferry in ten minutes. The museum
of clocks has more than four hundred clocks, and every clock in the museum is wound by hand on
Monday mornings. In winter the river sometimes freezes near the bank, and the ferry stops until
the ice has gone. The town council meets on the first Tuesday of every month, and the meetings
are open to everyone who lives in the town.
"""

ALPHABET = string.ascii_lowercase + " "


def clean(text: str) -> str:
    """Keep only lowercase letters and single spaces, as Shannon's examples did."""
    kept = "".join(ch if ch in ALPHABET else " " for ch in text.lower())
    return " ".join(kept.split())


def letters_order(text: str, context: int, length: int, rng: random.Random) -> str:
    """Generate `length` characters, each chosen given the previous `context` characters."""
    if context == 0:
        counts = Counter(text)
        symbols, weights = zip(*sorted(counts.items()))
        return "".join(rng.choices(symbols, weights, k=length))
    follows: dict[str, Counter] = defaultdict(Counter)
    for i in range(len(text) - context):
        follows[text[i:i + context]][text[i + context]] += 1
    out = text[:context]
    while len(out) < length:
        options = follows.get(out[-context:])
        if not options:  # a context never seen in the text: restart from the beginning
            out += " " + text[:context]
            continue
        symbols, weights = zip(*sorted(options.items()))
        out += rng.choices(symbols, weights)[0]
    return out[:length]


def words_order(text: str, context: int, count: int, rng: random.Random) -> str:
    """Generate `count` words, each chosen given the previous `context` words (0 or 1)."""
    words = text.split()
    if context == 0:
        return " ".join(rng.choice(words) for _ in range(count))
    follows: dict[str, list[str]] = defaultdict(list)
    for a, b in zip(words, words[1:]):
        follows[a].append(b)
    out = [words[0]]
    while len(out) < count:
        out.append(rng.choice(follows.get(out[-1]) or words))
    return " ".join(out)


def main() -> None:
    text = clean(TEXT)
    rng = random.Random(1948)
    print(f"source: {len(text.split())} words, {len(text)} characters\n")

    uniform = "".join(rng.choice(ALPHABET) for _ in range(60))
    print("letters, all equally likely     :", uniform)
    print("letters, by frequency           :", letters_order(text, 0, 60, rng))
    print("letters, 1 letter of context    :", letters_order(text, 1, 60, rng))
    print("letters, 2 letters of context   :", letters_order(text, 2, 60, rng))
    print("letters, 4 letters of context   :", letters_order(text, 4, 60, rng))
    print("words, by frequency             :", words_order(text, 0, 10, rng))
    print("words, 1 word of context        :", words_order(text, 1, 12, rng))


if __name__ == "__main__":
    main()

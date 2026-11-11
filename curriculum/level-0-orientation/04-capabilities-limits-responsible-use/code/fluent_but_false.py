"""Why generated text can be fluent but false, and how checking against sources catches it.

A tiny generator learns which word follows which from seven true sentences about the
fictional town of Brindlewick. Every sentence it writes is grammatical, because every
word-to-word step was seen in true text. But it has no idea which COMBINATIONS are true.

We then check each generated sentence against the sources:
  supported     -- the sources say exactly this
  contradicted  -- the sources give a different answer to the same question
  unsupported   -- the sources say nothing about it either way

A claim is keyed by its subject, verb and preposition, so "the market opens at six" (a time)
is a different question from "the market opens on saturday" (a day), not a contradiction.

Run:  python fluent_but_false.py

Expected output:
    the ferry leaves at ten        CONTRADICTED (sources: at seven)
    the ferry leaves at seven      supported
    the library opens at seven     CONTRADICTED (sources: at nine)
    the museum opens at eight      CONTRADICTED (sources: at ten)
    the ferry leaves at eight      CONTRADICTED (sources: at seven)
    the pool closes at nine        CONTRADICTED (sources: at eight)
    the market opens at six        unsupported
    the market closes at noon      supported

    Every sentence above is fluent. Checked against the sources:
      supported     2
      CONTRADICTED  5
      unsupported   1
"""

import random
from collections import defaultdict

SOURCES = [
    "the library opens at nine",
    "the library closes at six",
    "the market opens on saturday",
    "the market closes at noon",
    "the ferry leaves at seven",
    "the museum opens at ten",
    "the pool closes at eight",
]


def learn_next_words(sentences: list[str]) -> dict[str, list[str]]:
    follows: dict[str, list[str]] = defaultdict(list)
    for sentence in sentences:
        words = ["<start>"] + sentence.split() + ["<end>"]
        for current, nxt in zip(words, words[1:]):
            follows[current].append(nxt)
    return follows


def generate(follows: dict[str, list[str]], rng: random.Random) -> str:
    word, out = "<start>", []
    while True:
        word = rng.choice(follows[word])
        if word == "<end>":
            return " ".join(out)
        out.append(word)


def fact_key(sentence: str) -> tuple[tuple[str, str, str], str]:
    """Split 'the library closes at six' into (('library', 'closes', 'at'), 'six').

    The preposition is part of the question: 'at' asks for a time, 'on' asks for a day.
    """
    words = sentence.split()
    return (words[1], words[2], words[3]), " ".join(words[4:])


def check(sentence: str, facts: dict[tuple[str, str, str], str]) -> str:
    key, value = fact_key(sentence)
    if key not in facts:
        return "unsupported"
    return "supported" if facts[key] == value else f"CONTRADICTED (sources: {key[2]} {facts[key]})"


def main() -> None:
    facts = dict(fact_key(s) for s in SOURCES)
    follows = learn_next_words(SOURCES)
    rng = random.Random(3)

    seen: list[str] = []
    while len(seen) < 8:
        sentence = generate(follows, rng)
        if sentence not in seen:
            seen.append(sentence)

    tally: dict[str, int] = defaultdict(int)
    for sentence in seen:
        verdict = check(sentence, facts)
        tally[verdict.split()[0]] += 1
        print(f"{sentence:<30} {verdict}")
    print()
    print("Every sentence above is fluent. Checked against the sources:")
    for verdict in ("supported", "CONTRADICTED", "unsupported"):
        print(f"  {verdict:<13} {tally[verdict]}")


if __name__ == "__main__":
    main()

"""Solution (L0-01): how often does a tiny generator produce something new?

The generator only knows which word followed which. Every sentence it writes is built from
real word-to-word steps, but the whole sentence is often a combination nobody wrote.

Adding sentences gives the generator more "next word" options, so it usually produces a
higher share of new combinations, and more chances to state something untrue.

Run:  python new_or_copied.py

Expected output:
    5 training sentences: 69 copies, 131 new (66% new)
    8 training sentences: 39 copies, 161 new (80% new)
"""

import random
from collections import defaultdict

SENTENCES = [
    "the library opens at nine",
    "the market opens on saturday",
    "the library closes at six",
    "the ferry leaves at nine",
    "the market closes at noon",
]

EXTRA = [
    "the ferry leaves from the north pier",
    "the museum opens on sunday",
    "the pool closes at eight",
]


def learn_next_words(sentences):
    follows = defaultdict(list)
    for sentence in sentences:
        words = ["<start>"] + sentence.split() + ["<end>"]
        for current, nxt in zip(words, words[1:]):
            follows[current].append(nxt)
    return follows


def generate(follows, rng, max_words=10):
    word, out = "<start>", []
    while len(out) < max_words:
        word = rng.choice(follows[word])
        if word == "<end>":
            break
        out.append(word)
    return " ".join(out)


def count_new(sentences, n=200, seed=0):
    follows = learn_next_words(sentences)
    rng = random.Random(seed)
    copies = new = 0
    for _ in range(n):
        if generate(follows, rng) in sentences:
            copies += 1
        else:
            new += 1
    return copies, new


def main():
    for label, sentences in [("5 training sentences", SENTENCES),
                             ("8 training sentences", SENTENCES + EXTRA)]:
        copies, new = count_new(sentences)
        print(f"{label}: {copies} copies, {new} new ({100 * new / (copies + new):.0f}% new)")


if __name__ == "__main__":
    main()

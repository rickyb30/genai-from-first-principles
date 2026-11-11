"""Exercise (L0-01): how often does a tiny generator produce something new?

Goal: generate 200 sentences from the example sentences below and count how many are
  (a) exact copies of a training sentence, and
  (b) new combinations that never appeared in the training data.
Then add three sentences of your own to SENTENCES and run it again. Does the share of new
sentences go up or down? Why?

Fill in the two TODOs. The full solution is in solutions/new_or_copied.py.

Run:  python new_or_copied.py
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


def main():
    follows = learn_next_words(SENTENCES)
    rng = random.Random(0)
    copies = 0
    new = 0
    for _ in range(200):
        sentence = generate(follows, rng)
        # TODO 1: if the sentence is in SENTENCES, add 1 to copies; otherwise add 1 to new.
    # TODO 2: print both counts and the percentage of new sentences.


if __name__ == "__main__":
    main()

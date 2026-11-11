"""Three ways to get a computer to produce an output: rules, learning, and generation.

1. Conventional software: a person writes the rule.
2. Machine learning: the program works out its own rule from labelled examples.
3. Generative model: the program learns patterns from examples, then produces NEW text.

Everything here is deliberately tiny so you can read every line. Real systems use the same
ideas at a vastly larger scale.

Run:  python three_ways.py

Expected output:
    1. Rules written by a person
       'free prize meeting'        -> spam
       'team lunch moved'          -> ok
       'click to claim money'      -> ok
    2. Rules learned from 6 labelled examples
       'free prize meeting'        -> spam
       'team lunch moved'          -> ok
       'click to claim money'      -> spam
    3. New text generated from 5 example sentences
       the library closes at nine   (new)
       the market closes at nine   (new)
       the ferry leaves at nine
       the market closes at noon
       the library closes at noon   (new)
"""

import random
from collections import Counter, defaultdict

# --- 1. Conventional software: the rule is written by a person ---------------------------


def rule_based_filter(message: str) -> str:
    """A hand-written rule: any message containing 'free' or 'prize' is spam."""
    words = message.split()
    return "spam" if "free" in words or "prize" in words else "ok"


# --- 2. Machine learning: the rule comes from labelled examples --------------------------

EXAMPLES = [
    ("win a free prize now", "spam"),
    ("free money click now", "spam"),
    ("claim your prize today", "spam"),
    ("meeting moved to friday", "ok"),
    ("lunch with the team today", "ok"),
    ("notes from the friday meeting", "ok"),
]


def learn_word_counts(examples: list[tuple[str, str]]) -> dict[str, Counter]:
    """'Training': count how often each word appears in spam and in ok messages."""
    counts = {"spam": Counter(), "ok": Counter()}
    for text, label in examples:
        counts[label].update(text.split())
    return counts


def learned_filter(counts: dict[str, Counter], message: str) -> str:
    """Score a message: words seen more in spam push it towards spam, and vice versa."""
    score = sum(counts["spam"][w] - counts["ok"][w] for w in message.split())
    return "spam" if score > 0 else "ok"


# --- 3. Generation: learn which word tends to follow which, then write new sentences ------

SENTENCES = [
    "the library opens at nine",
    "the market opens on saturday",
    "the library closes at six",
    "the ferry leaves at nine",
    "the market closes at noon",
]


def learn_next_words(sentences: list[str]) -> dict[str, list[str]]:
    """For every word, record every word that followed it in the examples."""
    follows: dict[str, list[str]] = defaultdict(list)
    for sentence in sentences:
        words = ["<start>"] + sentence.split() + ["<end>"]
        for current, nxt in zip(words, words[1:]):
            follows[current].append(nxt)
    return follows


def generate(follows: dict[str, list[str]], rng: random.Random, max_words: int = 10) -> str:
    """Start at <start> and keep picking a plausible next word until <end>."""
    word, out = "<start>", []
    while len(out) < max_words:
        word = rng.choice(follows[word])
        if word == "<end>":
            break
        out.append(word)
    return " ".join(out)


def main() -> None:
    tests = ["free prize meeting", "team lunch moved", "click to claim money"]

    print("1. Rules written by a person")
    for t in tests:
        print(f"   {t!r:<27} -> {rule_based_filter(t)}")

    counts = learn_word_counts(EXAMPLES)
    print(f"2. Rules learned from {len(EXAMPLES)} labelled examples")
    for t in tests:
        print(f"   {t!r:<27} -> {learned_filter(counts, t)}")

    follows = learn_next_words(SENTENCES)
    rng = random.Random(6)  # fixed seed: the same "random" choices on every run
    print(f"3. New text generated from {len(SENTENCES)} example sentences")
    seen: set[str] = set()
    printed = 0
    while printed < 5:
        sentence = generate(follows, rng)
        if sentence in seen:
            continue
        seen.add(sentence)
        tag = "" if sentence in SENTENCES else "   (new)"
        print(f"   {sentence}{tag}")
        printed += 1


if __name__ == "__main__":
    main()

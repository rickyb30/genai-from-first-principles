"""Surprisal, entropy, cross-entropy, KL divergence and perplexity for Brindlewick's weather.

The true distribution of a day's weather is P = (sunny 0.5, cloudy 0.3, rain 0.2), from L1-02.
Several forecasters each claim a distribution Q. We measure how well each Q fits P.
Everything is in bits (logarithms base 2).

Run:  python entropy_and_friends.py

Expected output:
    surprisal of each outcome under P:
      sunny   p = 0.5   1.000 bits
      cloudy  p = 0.3   1.737 bits
      rain    p = 0.2   2.322 bits

    entropy:
      certain   (1.0, 0.0, 0.0)  0.000 bits
      weather   (0.5, 0.3, 0.2)  1.485 bits
      uniform   (1/3, 1/3, 1/3)  1.585 bits

    forecaster   Q                    cross-entropy   KL(P||Q)   perplexity
      honest     (0.50, 0.30, 0.20)      1.485 bits    0.000      2.800
      uniform    (0.33, 0.33, 0.33)      1.585 bits    0.099      3.000
      sunny-ish  (0.70, 0.20, 0.10)      1.618 bits    0.133      3.070
      no-rain    (0.60, 0.40, 0.00)        inf bits      inf        inf

    KL is not symmetric:
      KL(P || sunny-ish) = 0.133 bits
      KL(sunny-ish || P) = 0.123 bits
"""

import numpy as np

OUTCOMES = ["sunny", "cloudy", "rain"]
P = np.array([0.5, 0.3, 0.2])


def surprisal(p: np.ndarray) -> np.ndarray:
    """Bits of surprise when an outcome of probability p happens: -log2(p)."""
    with np.errstate(divide="ignore"):
        return -np.log2(p)


def entropy(p: np.ndarray) -> float:
    """Average surprisal under p itself. Outcomes with p = 0 contribute 0 (they never happen)."""
    nonzero = p > 0
    return float(np.sum(p[nonzero] * surprisal(p[nonzero])))


def cross_entropy(p: np.ndarray, q: np.ndarray) -> float:
    """Average surprisal when outcomes come from p but you score them with q."""
    nonzero = p > 0
    return float(np.sum(p[nonzero] * surprisal(q[nonzero])))


def kl_divergence(p: np.ndarray, q: np.ndarray) -> float:
    """Extra bits paid for using q instead of the true p: cross-entropy minus entropy."""
    return cross_entropy(p, q) - entropy(p)


def main() -> None:
    print("surprisal of each outcome under P:")
    for name, p, s in zip(OUTCOMES, P, surprisal(P)):
        print(f"  {name:<6}  p = {p:.1f}   {s:.3f} bits")

    print("\nentropy:")
    for label, shown, dist in [
        ("certain", "(1.0, 0.0, 0.0)", np.array([1.0, 0.0, 0.0])),
        ("weather", "(0.5, 0.3, 0.2)", P),
        ("uniform", "(1/3, 1/3, 1/3)", np.full(3, 1 / 3)),
    ]:
        print(f"  {label:<8}  {shown}  {entropy(dist):.3f} bits")

    forecasters = {
        "honest": P,
        "uniform": np.full(3, 1 / 3),
        "sunny-ish": np.array([0.7, 0.2, 0.1]),
        "no-rain": np.array([0.6, 0.4, 0.0]),
    }
    print("\nforecaster   Q                    cross-entropy   KL(P||Q)   perplexity")
    for name, q in forecasters.items():
        h = cross_entropy(P, q)
        shown = "(" + ", ".join(f"{x:.2f}" for x in q) + ")"
        print(f"  {name:<10} {shown:<20}  {h:>7.3f} bits  {kl_divergence(P, q):>7.3f}"
              f"    {2 ** h:>7.3f}")

    q = forecasters["sunny-ish"]
    print("\nKL is not symmetric:")
    print(f"  KL(P || sunny-ish) = {kl_divergence(P, q):.3f} bits")
    print(f"  KL(sunny-ish || P) = {kl_divergence(q, P):.3f} bits")


if __name__ == "__main__":
    main()

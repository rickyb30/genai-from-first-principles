"""Solution (L1-04): gradient checking. Find the hand-written gradient that's wrong.

Each function comes with a gradient someone derived by hand. A numerical estimate (central
differences) checks it. The relative error is the size of the difference divided by the size
of the two gradients, so it means the same thing for large and small gradients.
A relative error below about 1e-6 means the hand-written gradient is almost certainly right.

Run:  python check_my_gradient.py

Expected output:
    sum_of_squares         relative error below 1e-9   ok
    wave                   relative error below 1e-9   ok
    growth                 relative error 2.6e-01      WRONG
    softmax_cross_entropy  relative error below 1e-9   ok
"""

import numpy as np


def sum_of_squares(w):
    return float(np.sum(w ** 2))


def sum_of_squares_grad(w):
    return 2 * w


def wave(w):
    return float(np.sin(w[0]) * w[1])


def wave_grad(w):
    return np.array([np.cos(w[0]) * w[1], np.sin(w[0])])


def growth(w):
    return float(np.exp(w[0] * w[1]))


def growth_grad(w):
    e = np.exp(w[0] * w[1])
    return np.array([w[1] * e, e])          # bug: the second entry should be w[0] * e


def softmax_cross_entropy(z, target=0):
    p = np.exp(z) / np.exp(z).sum()
    return float(-np.log(p[target]))


def softmax_cross_entropy_grad(z, target=0):
    p = np.exp(z) / np.exp(z).sum()
    return p - np.eye(len(z))[target]


def numerical_gradient(func, w: np.ndarray, h: float = 1e-5) -> np.ndarray:
    """Central difference for each input in turn."""
    grad = np.zeros_like(w)
    for i in range(len(w)):
        step = np.zeros_like(w)
        step[i] = h
        grad[i] = (func(w + step) - func(w - step)) / (2 * h)
    return grad


def relative_error(a: np.ndarray, b: np.ndarray) -> float:
    """|a - b| / (|a| + |b|), with a tiny floor so two zero gradients don't divide by zero."""
    return float(np.linalg.norm(a - b) / max(np.linalg.norm(a) + np.linalg.norm(b), 1e-12))


CASES = [
    ("sum_of_squares", sum_of_squares, sum_of_squares_grad, np.array([0.5, -1.3, 2.0])),
    ("wave", wave, wave_grad, np.array([0.7, 1.5])),
    ("growth", growth, growth_grad, np.array([0.4, 0.9])),
    ("softmax_cross_entropy", softmax_cross_entropy, softmax_cross_entropy_grad,
     np.array([2.0, 1.0, 0.5])),
]


def main() -> None:
    for name, func, grad, w in CASES:
        err = relative_error(grad(w), numerical_gradient(func, w))
        verdict = "ok" if err < 1e-6 else "WRONG"
        shown = "below 1e-9" if err < 1e-9 else f"{err:.1e}"   # tiny values vary by machine
        print(f"{name:<22} relative error {shown:<10}   {verdict}")


if __name__ == "__main__":
    main()

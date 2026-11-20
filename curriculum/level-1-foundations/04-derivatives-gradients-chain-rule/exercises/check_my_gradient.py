"""Exercise (L1-04): gradient checking. Find the hand-written gradient that's wrong.

Each function below comes with a gradient someone derived by hand. One of them has a bug.
Your tasks:
  1. Complete numerical_gradient(): estimate each partial derivative with a central difference,
     (func(w + step) - func(w - step)) / (2h), where step is h in position i and 0 elsewhere.
  2. Complete relative_error(): |a - b| / (|a| + |b|), where |v| is np.linalg.norm(v).
  3. Run the file. Which gradient is wrong? Find the bug by redoing the derivative by hand.
  4. Stretch: change h to 1e-2 and then to 1e-12. What happens to the relative errors, and why?

The full solution is in solutions/check_my_gradient.py.

Run:  python check_my_gradient.py
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
    return np.array([w[1] * e, e])


def softmax_cross_entropy(z, target=0):
    p = np.exp(z) / np.exp(z).sum()
    return float(-np.log(p[target]))


def softmax_cross_entropy_grad(z, target=0):
    p = np.exp(z) / np.exp(z).sum()
    return p - np.eye(len(z))[target]


def numerical_gradient(func, w: np.ndarray, h: float = 1e-5) -> np.ndarray:
    """Central difference for each input in turn."""
    grad = np.zeros_like(w)
    # TODO: for each i, build `step` (zeros, with h at position i) and set
    # grad[i] = (func(w + step) - func(w - step)) / (2 * h).
    return grad


def relative_error(a: np.ndarray, b: np.ndarray) -> float:
    """|a - b| / (|a| + |b|), with a tiny floor so two zero gradients don't divide by zero."""
    # TODO: use np.linalg.norm, and max(..., 1e-12) for the floor.
    return float("nan")       # placeholder: until you finish this, every check prints WRONG


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

"""Derivatives as slopes, estimated with finite differences, and gradients of two-input functions.

A derivative tells you how fast a function's output changes when you nudge its input. You can
estimate it without any calculus: nudge the input by a small step h and measure the change.

Run:  python derivatives.py

Expected output:
    f(x) = x^3 at x = 2.0: exact derivative 3x^2 = 12.0
         h       forward    error       central    error
      0.1       12.61000  6.1e-01    12.01000  1.0e-02
      0.01      12.06010  6.0e-02    12.00010  1.0e-04
      0.001     12.00600  6.0e-03    12.00000  1.0e-06

    smaller is not always better (central difference):
      h = 1e-02   error 1.0e-04
      h = 1e-05   error 2.1e-10
      h = 1e-08   error 7.3e-08
      h = 1e-11   error 9.9e-07
      h = 1e-14   error 1.2e-01

    g(x, y) = x^2 + 3xy at (1, 2):
      gradient by hand:      [8. 3.]
      gradient by nudging:   [8. 3.]
"""

import numpy as np


def f(x: float) -> float:
    return x * x * x   # x cubed; plain multiplication rounds the same way on every machine


def forward_difference(func, x: float, h: float) -> float:
    """Slope from x to x + h."""
    return (func(x + h) - func(x)) / h


def central_difference(func, x: float, h: float) -> float:
    """Slope from x - h to x + h: a step each way, which cancels most of the error."""
    return (func(x + h) - func(x - h)) / (2 * h)


def numerical_gradient(func, point: np.ndarray, h: float = 1e-5) -> np.ndarray:
    """Estimate every partial derivative by nudging one input at a time (central differences)."""
    grad = np.zeros_like(point, dtype=float)
    for i in range(len(point)):
        step = np.zeros_like(point, dtype=float)
        step[i] = h
        grad[i] = (func(point + step) - func(point - step)) / (2 * h)
    return grad


def g(v: np.ndarray) -> float:
    x, y = v
    return x ** 2 + 3 * x * y


def main() -> None:
    x = 2.0
    exact = 3 * x ** 2
    print(f"f(x) = x^3 at x = {x}: exact derivative 3x^2 = {exact}")
    print("     h       forward    error       central    error")
    for h in [0.1, 0.01, 0.001]:
        fwd, cen = forward_difference(f, x, h), central_difference(f, x, h)
        print(f"  {h:<7}  {fwd:9.5f}  {abs(fwd - exact):.1e}   {cen:9.5f}  {abs(cen - exact):.1e}")

    print("\nsmaller is not always better (central difference):")
    for h in [1e-2, 1e-5, 1e-8, 1e-11, 1e-14]:
        cen = central_difference(f, x, h)
        print(f"  h = {h:.0e}   error {abs(cen - exact):.1e}")

    point = np.array([1.0, 2.0])
    exact_grad = np.array([2 * point[0] + 3 * point[1], 3 * point[0]])
    print("\ng(x, y) = x^2 + 3xy at (1, 2):")
    print(f"  gradient by hand:      {exact_grad}")
    print(f"  gradient by nudging:   {np.round(numerical_gradient(g, point), 6)}")


if __name__ == "__main__":
    main()

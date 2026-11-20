"""The chain rule, worked step by step: a forward pass to compute, a backward pass for gradients.

Part 1: L(w) = (2w - 6)^2, a function built from two small steps.
Part 2: L(w, b) = (w*x + b - y)^2, the squared error of a one-input model, plus one
        gradient-descent step to show the gradient pointing the way to a lower loss.
Part 3: the gradient of softmax followed by cross-entropy, which is simply p - y.
Each hand-derived gradient is checked against a numerical estimate.

Run:  python chain_rule_by_hand.py

Expected output:
    Part 1: L(w) = (2w - 6)^2 at w = 1
      forward:  u = 2w - 6 = -4.0   L = u^2 = 16.0
      backward: dL/du = 2u = -8.0   du/dw = 2   dL/dw = -16.0
      numerical check: -16.000000

    Part 2: L(w, b) = (w*x + b - y)^2 with x = 2, y = 7, w = 1, b = 0.5
      forward:  prediction z = 2.5   error r = -4.5   L = 20.25
      backward: dL/dr = -9.0   dL/dw = -18.0   dL/db = -9.0
      numerical check: dL/dw = -18.000000   dL/db = -9.000000
      one step downhill (step size 0.05): w = 1.90, b = 0.95, L = 5.0625

    Part 3: softmax then cross-entropy, scores [2.0, 1.0, 0.5], true outcome 0
      p = softmax(scores) = [0.629 0.231 0.14 ]   loss = 0.464 nats
      gradient p - y:      [-0.371  0.231  0.14 ]
      numerical check:     [-0.371  0.231  0.14 ]
"""

import numpy as np


def numerical_derivative(func, x: float, h: float = 1e-5) -> float:
    return (func(x + h) - func(x - h)) / (2 * h)


def part1() -> None:
    w = 1.0
    # Forward pass: compute and remember each intermediate value.
    u = 2 * w - 6          # inner step
    loss = u ** 2          # outer step
    # Backward pass: local derivatives, multiplied from the output back to the input.
    dloss_du = 2 * u       # d(u^2)/du
    du_dw = 2              # d(2w - 6)/dw
    dloss_dw = dloss_du * du_dw
    check = numerical_derivative(lambda v: (2 * v - 6) ** 2, w)
    print("Part 1: L(w) = (2w - 6)^2 at w = 1")
    print(f"  forward:  u = 2w - 6 = {u}   L = u^2 = {loss}")
    print(f"  backward: dL/du = 2u = {dloss_du}   du/dw = {du_dw}   dL/dw = {dloss_dw}")
    print(f"  numerical check: {check:.6f}")


def part2() -> None:
    x, y = 2.0, 7.0        # one training example: input 2, correct output 7
    w, b = 1.0, 0.5        # the model's current parameters

    def loss_of(w_: float, b_: float) -> float:
        return (w_ * x + b_ - y) ** 2

    z = w * x + b          # prediction
    r = z - y              # error
    loss = r ** 2
    dloss_dr = 2 * r
    dloss_dw = dloss_dr * x    # dz/dw = x
    dloss_db = dloss_dr * 1    # dz/db = 1
    print("\nPart 2: L(w, b) = (w*x + b - y)^2 with x = 2, y = 7, w = 1, b = 0.5")
    print(f"  forward:  prediction z = {z}   error r = {r}   L = {loss}")
    print(f"  backward: dL/dr = {dloss_dr}   dL/dw = {dloss_dw}   dL/db = {dloss_db}")
    print(f"  numerical check: dL/dw = {numerical_derivative(lambda v: loss_of(v, b), w):.6f}"
          f"   dL/db = {numerical_derivative(lambda v: loss_of(w, v), b):.6f}")

    step = 0.05
    w2, b2 = w - step * dloss_dw, b - step * dloss_db
    print(f"  one step downhill (step size {step}): w = {w2:.2f}, b = {b2:.2f}, "
          f"L = {loss_of(w2, b2):.4f}")


def part3() -> None:
    scores = np.array([2.0, 1.0, 0.5])
    target = 0                                     # the outcome that actually happened

    def loss_of(z: np.ndarray) -> float:
        p = np.exp(z) / np.exp(z).sum()
        return float(-np.log(p[target]))           # cross-entropy, in nats

    p = np.exp(scores) / np.exp(scores).sum()
    one_hot = np.eye(len(scores))[target]
    by_formula = p - one_hot
    numerical = np.array([
        numerical_derivative(lambda v, i=i: loss_of(np.where(np.arange(3) == i, v, scores)),
                             scores[i])
        for i in range(3)
    ])
    print("\nPart 3: softmax then cross-entropy, scores [2.0, 1.0, 0.5], true outcome 0")
    print(f"  p = softmax(scores) = {np.round(p, 3)}   loss = {loss_of(scores):.3f} nats")
    print(f"  gradient p - y:      {np.round(by_formula, 3)}")
    print(f"  numerical check:     {np.round(numerical, 3)}")


if __name__ == "__main__":
    part1()
    part2()
    part3()

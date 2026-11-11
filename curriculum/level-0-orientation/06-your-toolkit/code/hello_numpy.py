"""A first taste of NumPy: doing arithmetic on a whole list of numbers at once.

AI code is full of arrays: lists of numbers that are processed together. Here, one week of
noon temperatures (in °C) from Brindlewick's weather station shows the basic moves.

Run:  python hello_numpy.py

Expected output:
    temperatures (°C): [4.  6.5 7.  3.5 2.  5.  8. ]
    mean: 5.142857142857143
    warmest day index: 6 (0 = Monday)
    in °F: [39.2 43.7 44.6 38.3 35.6 41.  46.4]
    below 4 °C: [False False False  True  True False False] -> 2 days
    weighted mean: 5.44
"""

import numpy as np

temps_c = np.array([4.0, 6.5, 7.0, 3.5, 2.0, 5.0, 8.0])  # Monday to Sunday


def main() -> None:
    print("temperatures (°C):", temps_c)
    print("mean:", temps_c.mean())
    print("warmest day index:", int(temps_c.argmax()), "(0 = Monday)")

    # One expression converts all seven values. No loop needed.
    temps_f = temps_c * 9 / 5 + 32
    print("in °F:", temps_f)

    # Comparing an array to a number gives an array of True/False values.
    cold = temps_c < 4.0
    print("below 4 °C:", cold, "->", int(cold.sum()), "days")

    # A dot product multiplies matching items and adds them up. Here it weights each day.
    weights = np.array([1, 1, 1, 1, 1, 2, 2])  # count the weekend twice
    print("weighted mean:", round(float(temps_c @ weights / weights.sum()), 2))


if __name__ == "__main__":
    main()

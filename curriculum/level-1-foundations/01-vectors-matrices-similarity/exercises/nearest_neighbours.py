"""Exercise (L1-01): find each word's two nearest neighbours by cosine similarity.

The vocabulary now has 8 words and a fourth feature, "time". Your tasks:
  1. Complete cosine_matrix(): return an 8 x 8 matrix whose entry [i, j] is the cosine
     similarity between word i and word j. Use one matrix product, not a loop.
     Hint: normalize every row to length 1 first. What does U @ U.T compute?
  2. Complete top_k(): return the indices of the k most similar words to word `row`,
     leaving out the word itself.
  3. Before running, predict: which two words are the most similar pair? Which word is
     "clock" closest to?

The full solution is in solutions/nearest_neighbours.py.

Run:  python nearest_neighbours.py
"""

import numpy as np

WORDS = ["ferry", "boat", "river", "train", "museum", "library", "clock", "timetable"]
# Features:          water books travel time
W = np.array([
    [4, 0, 3, 1],   # ferry
    [3, 0, 4, 0],   # boat
    [5, 0, 0, 0],   # river
    [0, 0, 5, 2],   # train
    [0, 4, 3, 2],   # museum
    [0, 5, 0, 1],   # library
    [0, 1, 0, 5],   # clock
    [0, 1, 3, 4],   # timetable
], dtype=float)


def cosine_matrix(vectors: np.ndarray) -> np.ndarray:
    """Every pairwise cosine similarity, as a square matrix."""
    # TODO: divide each row by its length (np.linalg.norm with axis=1, keepdims=True),
    # then multiply the result by its own transpose.
    return np.zeros((len(vectors), len(vectors)))


def top_k(similarities: np.ndarray, row: int, k: int) -> list[int]:
    """Indices of the k most similar words to word `row`, excluding the word itself."""
    # TODO: sort the row's similarities from largest to smallest (np.argsort on the negated
    # row), skip `row` itself, and keep the first k indices.
    return []


def main() -> None:
    sims = cosine_matrix(W)
    print("similarity matrix shape:", sims.shape)
    print("diagonal (each word with itself):", np.round(np.diag(sims), 6))
    for i, word in enumerate(WORDS):
        neighbours = ", ".join(f"{WORDS[j]} ({sims[i, j]:.2f})" for j in top_k(sims, i, 2))
        print(f"{word:<10} -> {neighbours}")

    # Ignore the diagonal, then find the largest remaining entry.
    off_diagonal = sims - 2 * np.eye(len(WORDS))
    i, j = np.unravel_index(np.argmax(off_diagonal), off_diagonal.shape)
    print(f"most similar pair: {WORDS[i]} and {WORDS[j]} ({sims[i, j]:.2f})")


if __name__ == "__main__":
    main()

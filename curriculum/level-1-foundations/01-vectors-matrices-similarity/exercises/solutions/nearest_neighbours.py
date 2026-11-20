"""Solution (L1-01): find each word's nearest neighbours with one matrix product.

Normalizing every row to length 1 turns dot products into cosine similarities. Multiplying the
normalized matrix by its own transpose (U @ U.T) then gives every pair's cosine at once: entry
[i, j] is the cosine between word i and word j.

Run:  python nearest_neighbours.py

Expected output:
    similarity matrix shape: (8, 8)
    diagonal (each word with itself): [1. 1. 1. 1. 1. 1. 1. 1.]
    ferry      -> boat (0.94), river (0.78)
    boat       -> ferry (0.94), train (0.74)
    river      -> ferry (0.78), boat (0.60)
    train      -> timetable (0.84), boat (0.74)
    museum     -> library (0.80), timetable (0.76)
    library    -> museum (0.80), clock (0.38)
    clock      -> timetable (0.81), museum (0.51)
    timetable  -> train (0.84), clock (0.81)
    most similar pair: ferry and boat (0.94)
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
    unit = vectors / np.linalg.norm(vectors, axis=1, keepdims=True)
    return unit @ unit.T


def top_k(similarities: np.ndarray, row: int, k: int) -> list[int]:
    """Indices of the k most similar words to word `row`, excluding the word itself."""
    order = np.argsort(-similarities[row], kind="stable")  # most similar first
    return [int(j) for j in order if j != row][:k]


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

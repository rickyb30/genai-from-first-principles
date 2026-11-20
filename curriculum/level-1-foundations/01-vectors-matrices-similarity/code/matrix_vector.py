"""A matrix-vector product computes many dot products at once.

Stack the word vectors as the rows of a matrix. Multiplying that matrix by a query vector
gives the query's dot product with every word in one operation. Normalize the rows (and the
query) to length 1 first, and those dot products become cosine similarities. This is the core
of semantic search (L3-06), and the same operation, with learned numbers, runs inside every
layer of a neural network (L1-07).

Run:  python matrix_vector.py

Expected output:
    W has shape (6, 3): 6 words, 3 features each
    query "ferry" has shape (3,)
    W @ query has shape (6,): one score per word
    dot products:       [25. 24. 20. 15.  9.  0.]
    after normalizing:  [1.   0.96 0.8  0.6  0.36 0.  ]

    a 2 x 3 matrix that mixes features into 2 new ones:
    M = [[1 0 0]
         [0 1 1]]
    M @ ferry  = [4 3]
    M @ museum = [0 7]
"""

import numpy as np

WORDS = ["ferry", "boat", "river", "train", "museum", "library"]
# Rows are words. Columns are the features: water, books, travel.
W = np.array([
    [4, 0, 3],
    [3, 0, 4],
    [5, 0, 0],
    [0, 0, 5],
    [0, 4, 3],
    [0, 5, 0],
], dtype=float)


def normalize_rows(matrix: np.ndarray) -> np.ndarray:
    """Divide each row by its length, so every row has length 1."""
    return matrix / np.linalg.norm(matrix, axis=1, keepdims=True)


def main() -> None:
    query = W[0]  # "ferry"
    print(f"W has shape {W.shape}: {W.shape[0]} words, {W.shape[1]} features each")
    print(f'query "ferry" has shape {query.shape}')
    scores = W @ query
    print(f"W @ query has shape {scores.shape}: one score per word")
    print("dot products:      ", scores)

    # With unit-length rows and query, each dot product IS a cosine similarity.
    unit = normalize_rows(W)
    print("after normalizing: ", unit @ unit[0])

    # A matrix can also transform a vector: each output entry is a weighted sum of the inputs.
    # This one keeps "water" and merges "books" and "travel" into one "going out" feature.
    M = np.array([[1, 0, 0],
                  [0, 1, 1]])
    print("\na 2 x 3 matrix that mixes features into 2 new ones:")
    print("M =", str(M).replace("\n", "\n    "))
    print("M @ ferry  =", M @ W[0].astype(int))
    print("M @ museum =", M @ W[4].astype(int))


if __name__ == "__main__":
    main()

from fractions import Fraction
import numpy as np

def rref(matrix):
    tol = 1e-10  # Tolerance for floating-point comparisons
    lead = 0
    rowCount, columnCount = matrix.shape
    rank = 0  # Initialize rank
    for r in range(rowCount):
        if lead >= columnCount:
            return rank
        i = r
        while abs(matrix[i, lead]) < tol:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return rank
        matrix[[i, r]] = matrix[[r, i]]
        if abs(matrix[r, lead] - 0.0) > tol:
            matrix[r] /= matrix[r, lead]
        for i in range(rowCount):
            if i != r:
                matrix[i] -= matrix[i, lead] * matrix[r]
        lead += 1
        rank += 1  # Increment rank
    return rank

# Example usage:
# Define your matrix
A = np.array([[Fraction(1, 2), Fraction(3, 4), Fraction(1, 3)],
              [Fraction(2, 5), Fraction(1, 6), Fraction(5, 4)],
              [Fraction(3, 4), Fraction(2, 3), Fraction(7, 8)]], dtype=object)

print("Original matrix:")
print(A)
A = np.array([ [Fraction(1, 1), Fraction(0, 1)],
                     [Fraction(0, 1), Fraction(2, 1)],
                     [Fraction(1, 1), Fraction(1, 1)]], dtype=object)
A = A.transpose()
print(A)
# Compute RREF and rank
rank = rref(A)

print("\nMatrix in Reduced Row Echelon Form:")
print(A)
print("\nRank of the matrix:", rank)

I = np.array([[Fraction(1) if i == j else Fraction(0) for j in range(len(A[0]) - rank)] for i in range(len(A[0]) - rank)], dtype=object)

print("\nIdentity matrix I:")
print(I)

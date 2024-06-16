#!/usr/bin/env python3
"""
interview
"""


def rotate_2d_matrix(matrix):
    """
    Rotates the given n x n 2D matrix 90 degrees clockwise in place.

    Args:
    matrix (list of list of int): The n x n matrix to be rotated.

    Returns:
    None: The matrix is modified in place.
    """
    size = len(matrix)

    # Transpose the matrix: swap element at (row, col) with element
    # at (col, row)
    for r in range(size):
        for c in range(r, size):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    # Reverse each row to achieve the 90-degree rotation
    for row in range(size):
        matrix[row].reverse()
    return matrix

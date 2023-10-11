#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix.copy()
    for c in range(len(matrix)):
        new[c] = list(map(lambda x: x**2, matrix[c]))
    return new

#!/usr/bin/python3
"""A module to divide elements of a matrix"""


def matrix_divided(matrix, div):
    """A function to divide elements of matrix.

    Args:
        marix (int): matrix.
        div (int): num to divide elemnts of the matrix.
    Raises:
        TypeError: if args aren't integers or float or matrix rows
        size is not equal.
        ZeroDivisionError: if 0 is element of matrix.
    Returns:
        Quotient.
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix" + " (list of lists)"
                        + " of integers/floats")
    for r in matrix:
        if not isinstance(r, list) or len(r) == 0:
            raise TypeError("matrix must be a matrix (list of lists)"
                            + " of integers/floats")
        if len(r) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the "
                            + "same size")
        for c in r:
            if not isinstance(c, (int, float)):
                raise TypeError("matrix must be a matrix (list of"
                                + " lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(c / div, 2) for c in r] for r in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")

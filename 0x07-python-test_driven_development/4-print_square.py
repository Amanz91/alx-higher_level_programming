#!/usr/bin/python3
"""A module to print a square."""


def print_square(size):
    """A function to print a square.

    Args:
        size (int): size of square.
    Raises:
        TypeError: if size is not integer.
        ValueError: if size is < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("")
    else:
        for i in range(0, size):
            [print("#", end="") for j in range(size)]
            print("")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")

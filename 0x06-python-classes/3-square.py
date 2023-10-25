#!/usr/bin/python3
"""A module to define a square"""


class Square:
    """A class to represent a square"""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size (int): the length of a side of a square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is lessthan 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates area of a square.

        Returns:
            The size of the area.
        """
        return(self.__self ** 2)

#!/usr/bin/python3
"""A module for Square which inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class for square."""

    def __init__(self, size):
        """Intialize a square.
        Args:
            size (int): size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of Square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the str reprsentation of a rectangle."""
        s = "[" + str(self.__class__.__name__) + "] "
        s += str(self.__size) + "/" + str(self.__size)
        return s

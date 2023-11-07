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

#!/usr/bin/python3
"""A module for Rectangle which inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class for rectangle."""

    def __init__(self, width, height):
        """Intialize a rectangle.
        Args:
            width (int): width.
            height (int): height.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the str reprsentation of a rectangle."""
        s = "[" + str(self.__class__.__name__) + "] "
        s += str(self.__width) + "/" + str(self.__height)
        return s

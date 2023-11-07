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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

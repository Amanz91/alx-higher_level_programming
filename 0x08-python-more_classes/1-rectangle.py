#!/usr/bin/python3
"""Module to define a rectangle"""


class Rectangle:
    """Class to define a rectangle"""
    def __init__(self, width=0, height=0):
        """Intialize a an object of rectangle.

        Args:
            width (int): width of rectangle.
            height (int): height of rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the size of a rectangle.

        Returns:
            width of the recatngle.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the width of rectangle.

        Args:
            value (int): width.
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is lessthan 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of a rectangle.

        Returns:
            height of the recatngle.
        """
        return (self.__height)

    @width.setter
    def height(self, value):
        """Sets the height of rectangle.

        Args:
            value (int): height.
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is lessthan 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

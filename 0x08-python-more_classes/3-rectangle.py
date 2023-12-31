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
        self.height = height
        self.width = width

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

    @height.setter
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

    def area(self):
        """Calculates area of a rectangle.

        Returns:
            The area of recatngle.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates perimeter of rectangle.

        Returns:
            The perimeter of recatangle or 0 if
            width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns a printable string reprsentation of recatangle."""
        if self.__width == 0 or self.__height == 0:
            return ("")
        r = []
        for i in range(0, self.__height):
            [r.append("#") for j in range(0, self.__width)]
            if i != self.__height - 1:
                r.append("\n")
        return ("".join(r))

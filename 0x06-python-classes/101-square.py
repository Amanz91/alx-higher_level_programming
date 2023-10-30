#!/usr/bin/python3
"""A module to define a square"""


class Square:
    """A class to represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor.

        Args:
            size (int): the length of a side of a square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the size of a side of square.

        Returns:
            The size of the side.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets size of a side of a square.

        Args:
            size (int): the length of a side of a square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is lessthan 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets position of a square.

        Args:
           position (int):  a tuple of 2 positive integers.
        Raises:
           TypeError: if not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates area of a square.

        Returns:
            The size of the area.
        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints a square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")

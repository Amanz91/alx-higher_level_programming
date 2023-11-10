#!/usr/bin/python3
"""A module to define a subclass Rectangle."""
from models.base import Base


class Rectangle(Base):
    """A sub class rectangle of class base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor to intialize an instance of Rectangle.
        Args:
            width (int): width.
            height (int): height.
            x (int): x.
            y (int): y.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Method to calculate area"""
        return self.__width * self.__height

    def update(self, *args, **kwargs):
        """Method to update attributes of rectangle.
        Args:
            *args (int): New values to update.
                - 1st argument is id attribute
                - 2nd argument is width attribute
                - 3rd argument is height attribute
                - 4th argument is x attribute
                - 5th argument is y attribute
        """
        if args and len(args) != 0:
            v = 0
            for arg in args:
                if v == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x,
                                      self.y)
                    else:
                        self.id = arg
                elif v == 1:
                    self.width = arg
                elif v == 2:
                    self.height = arg
                elif v == 3:
                    self.x = arg
                elif v == 4:
                    self.y = arg
                v += 1
        elif kwargs and len(kwargs) != 0:
            for k, i in kwargs.items():
                if k == "id":
                    if i is None:
                        self.__init__(self.width, self.height, self.x,
                                      self.y)
                    else:
                        self.id = i
                elif k == "width":
                    self.width = i
                elif k == "height":
                    self.height = i
                elif k == "x":
                    self.x = i
                elif k == "y":
                    self.y = i

    def display(self):
        """A function to print a rectangle with '#'."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

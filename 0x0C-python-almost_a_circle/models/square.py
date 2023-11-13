#!/usr/bin/python3
"""A module to define a subclass Square."""
from models.rectangle import Rectangle


class Squae(Rectangle):
    """A sub class square of class rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor to intialize an instance of square.
        Args:
            size (int): size.
            x (int): x.
            y (int): y.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method to update attributes of rectangle.
        Args:
            *args (int): New values to update.
                - 1st argument is id attribute
                - 2nd argument is size attribute
                - 3rd argument is x attribute
                - 4th argument is y attribute
            **kwargs (dict): New keys-values
        """
        if args and len(args) != 0:
            v = 0
            for arg in args:
                if v == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif v == 1:
                    self.size = arg
                elif v == 2:
                    self.x = arg
                elif v == 3:
                    self.y = arg
                v += 1
        elif kwargs and len(kwargs) != 0:
            for k, i in kwargs.items():
                if k == "id":
                    if i is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = i
                elif k == "size":
                    self.size = i
                elif k == "x":
                    self.x = i
                elif k == "y":
                    self.y = i

    def to_dictionary(self):
        """Return the dictionary representation of a square."""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "size": self.size
        }

    def __str__(self):
        """Return the print() and str() representation of square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

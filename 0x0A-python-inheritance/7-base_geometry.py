#!/usr/bin/python3
"""A module for geometry."""


class BaseGeometry:
    """A class for geometry."""
    def area(self):
        """Function not implrmrnted."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A function to validate value.
        Args:
            name (str): name of var.
            value (int): integer value > 0.
        Raises:
            TypeError: if value isn't integer.
            ValueError: if value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0"
                             .format(name))

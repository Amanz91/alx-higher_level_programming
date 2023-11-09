#!/usr/bin/python3
"""A module to define clase Base."""


class Base:
    """A new class Base."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for instances of calss Base.
        Args:
            id (int): id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

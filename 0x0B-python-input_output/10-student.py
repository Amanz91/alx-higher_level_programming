#!/usr/bin/python3
"""Module returns the dictionary description of class student."""


class Student:
    """A class to define Student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, a=None):
        """Return the dictionary represntation of a student."""
        if type(a) == list and all(type(e) == str for e in a):
            return {ls: getattr(self, ls) for ls in a if hasattr(self, ls)
        return self.__dict__

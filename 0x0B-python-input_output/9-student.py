#!/usr/bin/python3
"""Module returns the dictionary description of class student."""


class Student:
    """A class to define Student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        sel.age = age

    def to_json(self):
    """Return the dictionary represntation of a student."""
    return self.__dict__

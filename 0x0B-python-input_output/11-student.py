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
        try:
            for attr in a:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        d = dict()
        for k, value in self.__dict__.items():
            if k in a:
                d[k] = value
        return d

    def reload_from_json(self, json):
        """Func to replace all attrs of student instance."""
        for k, value in json.items():
            if k in self.__dict__:
                self.__dict__[k] = value

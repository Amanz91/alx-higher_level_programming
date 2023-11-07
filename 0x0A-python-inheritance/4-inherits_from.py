#!/usr/bin/python3
"""A module checks object is exactly an instance of class."""


def inherits_from(obj, a_class):
    """A function to check object's class."""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

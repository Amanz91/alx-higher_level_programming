#!/usr/bin/python3
"""A module checks object is exactly an instance of class."""


def inherits_from(obj, a_class):
    """A function to check object's class."""

    if isinstance(obj, a_class) or type(obj) == a_class:
        return True
    return False

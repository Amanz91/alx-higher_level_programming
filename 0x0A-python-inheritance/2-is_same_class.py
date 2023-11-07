#!/usr/bin/python3
"""A module checks object is exactly an instance of class."""


def is_same_class(obj, a_class):
    """A function to check object's class."""

    if type(obj) == a_class:
        return True
    return False

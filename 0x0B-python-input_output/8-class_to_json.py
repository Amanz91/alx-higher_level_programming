#!/usr/bin/python3
"""Module returns the dictionary description with simple data
structure"""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure
    Args:
        obj (obj): instance of a class
    Returns:
        a dictionary representation
    """
    return obj.__dict__

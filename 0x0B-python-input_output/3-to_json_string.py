#!/usr/bin/python3
"""A module to return the JSON representation of an object."""
import json


def to_json_string(my_obj):
    """Func to return the JSON representation of an object.
    Args:
        my_obj (str): text to be converted.
    """
    return (json.dumps(my_obj))

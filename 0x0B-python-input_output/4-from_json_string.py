#!/usr/bin/python3
"""A module to return the JSON representation to an object."""
import json


def from_json_string(my_str):
    """Func to return the JSON representation to an object.
    Args:
        my_obj (str): text to be converted.
    """
    return (json.loads(my_str))

#!/usr/bin/python3
"""A module to create an object from JSON file."""
import json


def load_to_json_file(filename):
    """Func to create an object from JSON file.
    Args:
        filename (str): filename.
    """
    with open(filename) as f:
        return json.load(f)

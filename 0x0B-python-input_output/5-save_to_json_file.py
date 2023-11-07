#!/usr/bin/python3
"""A module to write an object to text file and return JSON rep."""
import json


def save_to_json_file(my_obj, filename):
    """Func to write an object in JSON to text file.
    Args:
        my_obj (obj): object to be converted.
        filename (str): filename.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)

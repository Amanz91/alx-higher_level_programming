#!/usr/bin/python3
"""A module to open a file in write mode and write content."""


def write_file(filename="", text=""):
    """Func to open a file in write mode and write content.
    Args:
        filename (str): filename.
        text (str): text to be written to file.
    """
    with open(filename, encoding="utf-8") as f:
        return (f.write(text), end="")

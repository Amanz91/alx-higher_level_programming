#!/usr/bin/python3
"""A module to open a file in append mode and append content."""


def append_write(filename="", text=""):
    """Func to open a file in append mode and write content.
    Args:
        filename (str): filename.
        text (str): text to be written to file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))

#!/usr/bin/python3
"""A module to open a file in read mode and print its content."""


def read_file(filename=""):
    """Func to open a file in read mode and print its content.
    Args:
        filename (str): filename.
    """
    with open('filename', encoding="utf-8") as f:
        red_d = f.read()
        print(red_d)

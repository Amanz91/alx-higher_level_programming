#!/usr/bin/python3
"""A module to list available attributes and methods."""


def lookup(obj):
    """Returns a list of available attributes and methods."""
    return (dir(obj))

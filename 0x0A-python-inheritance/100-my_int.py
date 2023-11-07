#!/usr/bin/python3
"""A module for class Myint."""


class MyInt(int):
    """A sub-class of the in-built class int."""

    def __eq__(self, value):
        """Func to override == op with != op."""
        return sel.real != value

    def __ne__(self, value):
        """Func to override != op with == op."""
        return sel.real == value

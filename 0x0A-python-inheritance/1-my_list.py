#!/usr/bin/python3
"""A module that prints the list, but sorted."""


class MyList(list):
    """A sub-class of the in-built class list."""

    def print_sorted(self):
        """ Prints a sorted list."""
        print(sorted(self))

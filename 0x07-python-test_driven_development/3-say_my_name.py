#!/usr/bin/python3
"""A module to print full name."""


def say_my_name(first_name, last_name=""):
    """A function to print full name.

    Args:
        first_name (str): first name.
        last_name (str): last name.
    Raises:
        TypeError: if first_name and last_name must be strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is " + first_name + " " + last_name)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")

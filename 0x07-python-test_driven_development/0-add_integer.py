#!/usr/bin/python3
"""A module to add two integers"""

def add_integer(a, b=98):
    """A function to add two integers.

    Args:
        a (int): 1st num.
        b (int): 2nd num.
    Raises:
        TypeError: if args aren't integers or float.
    Returns:
        Sum.
    """
    if ((not isinsatance(a, int) and not isinsatance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinsatance(b, int) and not isinsatance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

#!/usr/bin/python3
"""A module that defines a locked class."""


class LockedClass:
    """A class that prevents the user from instantiating new
    LockedClass attributes for anything but attributes 
    called "first_name".
    """

    __names__ = ["first_name"]

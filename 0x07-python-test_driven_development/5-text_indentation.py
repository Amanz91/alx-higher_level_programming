#!/usr/bin/python3
"""A module to indent a text."""


def text_indentation(text):
    """A function to indent a string.

    Args:
        text (str): text to indent.
    Raises:
        TypeError: if text is not a string.
     """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for d in ".?:":
        text = (d + "\n\n").join(
                [line.strip(" ") for line in text.split(d)])
    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")

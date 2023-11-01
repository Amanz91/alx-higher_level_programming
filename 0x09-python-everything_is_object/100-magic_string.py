#!/usr/bin/python3
def magic_string():
    c = getattr(magic_string, "c", 0)
    magic_string.c = c + 1
    return "BestSchool" + (", BestSchool" * c)

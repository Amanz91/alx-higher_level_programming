#!/usr/bin/python3
def no_c(my_string):
    if len(my_string) != 0:
        new = my_string.translate({ord(i): None for i in 'cC'})
        return new
    else:
        return my_string

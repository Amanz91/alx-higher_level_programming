#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    l_new = list(a_dictionary.keys())
    l_new.sort()
    for i in l_new:
        print("{}: {}".format(i, a_dictionary.get(i)))

#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    k = sorted(a_dictionary.keys())
    for i, c in k.items():
        print("{}: {}".format(i, c))

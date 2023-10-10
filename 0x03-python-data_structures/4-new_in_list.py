#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    c = len(my_list)
    new = my_list.copy()
    for n in range(len(new)):
        if idx < 0 or idx > c - 1:
            return new
        new[idx] = element
        return new

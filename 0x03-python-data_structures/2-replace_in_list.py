#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    c = len(my_list)
    for n in range(len(my_list)):
        if idx < 0 or idx > c - 1:
            return my_list
        my_list[idx] = element
        return my_list

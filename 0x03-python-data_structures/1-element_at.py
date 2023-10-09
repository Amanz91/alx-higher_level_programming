#!/usr/bin/python3
def element_at(my_list, idx):
    c = len(my_list)
    for n in range(len(my_list)):
        if idx < 0 or idx > c - 1:
            return None
        return my_list[idx]

#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    c = len(my_list)
    for n in range(len(my_list)):
        if idx < 0 or idx > c - 1 or c == 0:
            return my_list
        else:
            del my_list[idx]
            return my_list

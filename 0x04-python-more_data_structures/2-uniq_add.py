#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    new = 0
    for i in new_list:
        new += i
    return new

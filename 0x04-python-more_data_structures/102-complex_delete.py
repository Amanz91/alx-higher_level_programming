#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    k_list = list(a_dictionary.keys())
    for value in k_list:
        if value == a_dictionary.get(v):
            del a_dictionary[v]
    return a_dictionary

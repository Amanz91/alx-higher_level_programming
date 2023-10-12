#!/usr/bin/python3
def best_score(a_dictionary):
    for k, v in a_dictionary.items():
        if v is None:
            return None
    return (max(a_dictionary, key=a_dictionary.get))

#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if not a_dictionary:  # Check if the dictionary is empty
        return None

    max_value = None
    for value in a_dictionary.values():
        if max_value is None or value > max_value:
            max_value = value

    return max_value

#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Return new dictionary with values multiplied by 2."""
    return {k: v * 2 for k, v in a_dictionary.items()}

#!/usr/bin/python3
def best_score(a_dictionary):
    """Return key with biggest integer value."""
    if not a_dictionary:
        return None
    best_key = None
    max_val = float(-inf)
    for k, v in a_dictionary.items():
        if v > max_val:
            max_val = v
            best_key = k
    return best_key

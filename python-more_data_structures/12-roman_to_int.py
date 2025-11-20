#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Converts a Roman numeral string to an integer.
    Args:
        roman_string: A string representing a Roman numeral (1-3999)
    Returns:
        An integer value of the Roman numeral, or 0 if invalid input
    """
    if not isinstance(roman_string, str):
        return 0

    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}

    total = 0
    prev = 0

    for char in reversed(roman_string):
        if char not in roman_map:
            return 0
        value = roman_map[char]
        if value < prev:
            total -= value
        else:
            total += value
        prev = value

    return total

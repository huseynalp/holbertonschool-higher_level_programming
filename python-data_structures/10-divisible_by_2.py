#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list.

    Returns a new list of True/False values corresponding to whether
    each integer in the original list is a multiple of 2.
    """
    result = []
    for num in my_list:
        result.append(num % 2 == 0)
    return result

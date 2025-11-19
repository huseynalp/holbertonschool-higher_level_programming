#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Make a copy of the list
    new_list = my_list.copy()

    # Check invalid index
    if idx < 0 or idx >= len(new_list):
        return new_list

    # Replace element in the copy
    new_list[idx] = element

    return new_list

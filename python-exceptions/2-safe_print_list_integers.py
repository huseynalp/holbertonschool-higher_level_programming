#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of my_list that are integers.
    Returns the number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            value = my_list[i]
            print("{:d}".format(value), end="")
            count += 1
        except (ValueError, TypeError):
            # Skip non-integers silently
            pass
        except IndexError:
            # Stop if i exceeds list length
            break
    print()
    return count

#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divides two integers a and b.
    Prints the result in the finally block as "Inside result: <result>".
    Returns the division result, or None if division fails.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result

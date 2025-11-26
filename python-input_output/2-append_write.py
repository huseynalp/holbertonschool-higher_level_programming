#!/usr/bin/python3
"""Function that appends text to the end of a file."""


def append_write(filename="", text=""):
    """Appends a string to a UTF8 text file and returns number of characters."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

#!/usr/bin/python3
"""Function that appends text to a UTF-8 file."""


def append_write(filename="", text=""):
    """Append a string at the end of a UTF-8 text file."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

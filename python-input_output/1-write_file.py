#!/usr/bin/python3
"""Module that writes a string to a text file."""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file and returns the character count."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

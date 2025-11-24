#!/usr/bin/python3
"""Module that defines a MyList class inheriting from list."""


class MyList(list):
    """Represents a list with an additional method to print it sorted."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))

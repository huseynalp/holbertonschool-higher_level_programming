#!/usr/bin/python3
"""Module defining a Student class with JSON serialization support."""


class Student:
    """Represents a student with basic attributes."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes in that list
        are included. Otherwise, all attributes are included.
        """
        if isinstance(attrs, list) and all(
            isinstance(a, str) for a in attrs
        ):
            return {
                k: v
                for k, v in self.__dict__.items()
                if k in attrs
            }
        return self.__dict__.copy()

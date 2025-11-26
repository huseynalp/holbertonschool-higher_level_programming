#!/usr/bin/python3
"""Function that returns the JSON representation of an object."""

import json


def to_json_string(my_obj):
    """Return the JSON representation of a Python object (as a string)."""
    return json.dumps(my_obj)

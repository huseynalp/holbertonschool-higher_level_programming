#!/usr/bin/python3
"""Function that returns a Python object represented by a JSON string."""

import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string."""
    return json.loads(my_str)

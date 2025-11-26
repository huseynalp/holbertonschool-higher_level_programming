#!/usr/bin/python3
"""Function that creates a Python object from a JSON file."""

import json


def load_from_json_file(filename):
    """Load an object from a JSON file and return it."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves them to a file."""

import sys
from pathlib import Path

save_to_json_file = __import__(
    '5-save_to_json_file'
).save_to_json_file
load_from_json_file = __import__(
    '6-load_from_json_file'
).load_from_json_file

FILENAME = "add_item.json"

# Load existing list or start with empty
if Path(FILENAME).exists():
    my_list = load_from_json_file(FILENAME)
else:
    my_list = []

# Add all arguments (excluding the script name)
args_to_add = sys.argv[1:]
my_list.extend(args_to_add)

# Save the updated list back to the JSON file
save_to_json_file(my_list, FILENAME)

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

# Check if the file exists; if yes, load the list, otherwise start with an empty list
if Path(FILENAME).exists():
    my_list = load_from_json_file(FILENAME)
else:
    my_list = []

# Add all arguments (excluding the script name)
my_list.extend(sys.argv[1:])

# Save the updated list back to the JSON file
save_to_json_file(my_list, FILENAME)

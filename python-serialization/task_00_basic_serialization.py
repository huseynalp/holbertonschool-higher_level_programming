#!/usr/bin/env python3
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file.
    
    Parameters:
        data (dict): The dictionary to serialize.
        filename (str): The JSON output filename.
    """
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize it into a Python dictionary.
    
    Parameters:
        filename (str): The JSON input filename.
        
    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, "r") as f:
        return json.load(f)

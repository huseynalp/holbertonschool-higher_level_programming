#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts CSV data into JSON format and saves it to data.json.

    Parameters:
        csv_filename (str): Name of the input CSV file.

    Returns:
        bool: True if conversion succeeded, False otherwise.
    """
    try:
        data_list = []

        # Read the CSV file using DictReader
        with open(csv_filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_list.append(row)

        # Serialize to JSON and save to data.json
        with open("data.json", "w") as jsonfile:
            json.dump(data_list, jsonfile, indent=4)

        return True

    except Exception:
        return False


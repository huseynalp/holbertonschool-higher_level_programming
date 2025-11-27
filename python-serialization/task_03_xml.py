#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into an XML file.

    Parameters:
        dictionary (dict): The data to serialize.
        filename (str): The XML output filename.
    """
    try:
        # Create root <data> element
        root = ET.Element("data")

        # Add each dictionary key-value pair as a child element
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)  # Ensure text is a string

        # Create and write the XML tree to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=False)

        return True

    except Exception:
        return False


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.

    Parameters:
        filename (str): The XML input filename.

    Returns:
        dict: The reconstructed dictionary, or None on failure.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        data = {}

        # Each child corresponds to a dictionary entry
        for child in root:
            data[child.tag] = child.text  # Values remain strings

        return data

    except Exception:
        return None

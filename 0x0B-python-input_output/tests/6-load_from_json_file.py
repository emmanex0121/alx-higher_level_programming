#!/usr/bin/python3
"""Module definining Object creation from JSON file"""
import json


def load_from_json_file(filename):
    """Creates and Object from a JSON file"""
    with open(filename, encoding="UTF8") as f:
        return json.load(f)

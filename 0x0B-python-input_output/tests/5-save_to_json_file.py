#!/usr/bin/python3
"""Module contains JSON implementation of writing to files"""
import json


def save_to_json_file(my_obj, filename):
    """Writes JSON object representation to file"""
    with open(filename, "w", encoding="UTF*") as f:
        json.dump(my_obj, f)

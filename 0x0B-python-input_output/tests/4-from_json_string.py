#!/usr/bin/python3
"""Module that defines json representation of python Data Structure"""
import json


def from_json_string(my_str):
    """Return JSON representation of Python data structure object"""
    return json.loads(my_str)

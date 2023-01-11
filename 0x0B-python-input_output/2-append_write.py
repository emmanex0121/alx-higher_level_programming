#!/usr/bin/python3
"""Module defining appending function to file"""


def append_write(filename="", text=""):
    """Append string to file contents"""
    with open(filename, 'a', encoding='UTF8') as f:
        return f.write(text)

#!/usr/bin/python3
"""Modeule defining writing to file"""

def write_file(filename="", text=""):
    """Writes strings to files and return number of characters written"""
    with open(filename, "w", encoding="UTF8") as f:
        return f.write(text)

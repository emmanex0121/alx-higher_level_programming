#!/usr/bin/python3
"""Module that adds and appends all python stdin arguments to list"""
import json
import sys
argv = sys.argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


try:
    contents = load_from_json_file("add_item.json")
except FileNotFoundError:
    contents = []
    save_to_json_file(contents, "add_item.json")

contents += argv[1:]
save_to_json_file(contents, "add_item.json")

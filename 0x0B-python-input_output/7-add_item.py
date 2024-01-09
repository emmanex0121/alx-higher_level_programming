#!/usr/bin/python3
# Program By Phoenix
""" Scripts that adds and appends all command line inputs to list"""
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


a = []
a = argv[1:]
# for i in range(1, len(argv)):
# a.append(argv[i])

try:
    a = load_from_json_file('add_item.json') + a
except FileNotFoundError:
    save_to_json_file(a, 'add_item.json')
else:
    save_to_json_file(a, 'add_item.json')

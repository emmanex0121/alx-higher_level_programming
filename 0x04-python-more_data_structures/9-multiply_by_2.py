#!/usr/bin/python3
# Program By Phoenix

def multiply_by_2(a_dictionary):
    new_dict = {}
    for key in a_dictionary:
        new_dict[key] = a_dictionary[key] * 2
    return new_dict

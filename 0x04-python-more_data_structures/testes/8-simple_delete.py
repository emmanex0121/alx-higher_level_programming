#!/usr/bin/python3
# Program By Phoenix

def simple_delete(a_dictionary, key=""):
    for k in a_dictionary:
        if k == key:
            del a_dictionary[key]
            return a_dictionary
    return a_dictionary

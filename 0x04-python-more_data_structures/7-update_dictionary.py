#!/usr/bin/python3
# Program By Phoenix

def update_dictionary(a_dictionary, key, value):
    for k in a_dictionary:
        if k == key:
            a_dictionary[k] = value
            return a_dictionary
    else:
        a_dictionary[key] = value
        return a_dictionary

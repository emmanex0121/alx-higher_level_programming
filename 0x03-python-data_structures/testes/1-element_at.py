#!/usr/bin/python3
# Program By Phoenix

def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return None
    return my_list[idx]

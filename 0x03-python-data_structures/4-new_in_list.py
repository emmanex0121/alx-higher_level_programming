#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    mod_list = my_list.copy()
    if idx < 0 or idx > len(mod_list) - 1:
        return mod_list
    else:
        mod_list[idx] = element
        return mod_list

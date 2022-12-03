#!/usr/bin/python3

def no_c(my_string):
    str = ""
    for element in my_string:
        if element != 'c' and element != 'C':
            str += element
    return str
    """
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            my_string = my_string[:i] + my_string[i+1:]
        else:
            my_string = my_string
    return my_string
    """

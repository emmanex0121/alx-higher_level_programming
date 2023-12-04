#!/usr/bin/python3
# Program By Phoenix

def print_reversed_list_integer(my_list=[]):
    for element in my_list[::-1]:
        print("{:d}".format(element))

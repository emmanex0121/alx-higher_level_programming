#!/usr/bin/python3
# Program By Phoenix

def print_reversed_list_integer(my_list=[]):
    if my_list:
        for num in reversed(my_list):
            print('{:d}'.format(num))

    '''
        OR THIS WAY
    my_list.reverse()
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
    OR THIS

    def print_reversed_list_integer(my_list=[]):
        for element in my_list[::-1]:
            print("{:d}".format(element))
    '''

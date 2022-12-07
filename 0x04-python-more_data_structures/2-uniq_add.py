#!/usr/bin/python3

def uniq_add(my_list=[]):
    num = 0
    my_list = set(my_list)
    print(my_list)
    for n in my_list:
        num += n
    return num

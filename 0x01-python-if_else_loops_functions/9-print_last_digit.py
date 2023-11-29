#!/usr/bin/python3
# Program By Phoenix

def print_last_digit(number):
    if number < 0:
        last_num = -number % 10
    else:
        last_num = number % 10
    print("{}".format(last_num))
    return last_num

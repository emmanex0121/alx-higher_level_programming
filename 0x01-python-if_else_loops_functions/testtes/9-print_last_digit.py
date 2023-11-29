#!/usr/bin/python3
# Program By Phoenix

def print_last_digit(number):
    if number < 0:
        return (-1 * number) % 10
    return number % 10

#!/usr/bin/python3

for digit1 in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
        if digit1 is 8 and digit2 is 9:
            print("{:d}{:d}".format(digit1, digit2))
        else:
            print("{:d}{:d}".format(digit1, digit2), end=', ')

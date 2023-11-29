#!/usr/bin/python3
# Program by Phoenix

for num in range(100):
    if num == 99:
        print("{:02}".format(num))
    else:
        print("{:02}".format(num), end=', ')

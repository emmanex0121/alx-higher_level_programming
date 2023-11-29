#!/usr/bin/python3
# Program By Phoenix

def uppercase(str):
    for i in range(len(str)):
        if str[i] in ' 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            num = 0
        else:
            num = 32
        print("{:c}".format(ord(str[i]) - num), end='')
    print()

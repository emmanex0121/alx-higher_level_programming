#!/usr/bin/python3
# Program By Phoenix
if __name__ == '__main__':
    from sys import argv

if len(argv) < 2:
    print("0")
else:
    sum_all = 0
    for i in range(1, len(argv)):
        sum_all += int(argv[i]);
    print(sum_all)

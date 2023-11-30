#!/usr/bin/python3
# Program By Phoenix
if __name__ == '__main__':
    from sys import argv

if len(argv) < 1:
    print("0 arguments.")
else:
    print(f"{len(argv) - 1} arguments:")
    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")

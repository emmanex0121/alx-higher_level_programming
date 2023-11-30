#!/usr/bin/python3
# Program By Phoenix
if __name__ == '__main__':
    from sys import argv

if len(argv) < 2:
    print("0 arguments.")
elif len(argv) == 2:
    print(f"1 argument:")
    print(f"1: {argv[1]}")
else:
    print(f"{len(argv) - 1} arguments:")
    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")

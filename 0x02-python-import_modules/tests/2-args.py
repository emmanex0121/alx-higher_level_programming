#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv

if len(argv) == 2:
    print("{:d} argument:".format(len(argv) - 1))
else:
    print("{:d} arguments:".format(len(argv) - 1))

for i in range(1, len(argv)):
    count = i
    print("{:d}: {}".format(i, argv[i]))

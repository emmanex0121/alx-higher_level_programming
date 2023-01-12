#!/usr/bin/python3
import sys
argv = sys.argv

s = []
t = 0
for args in range(1, len(argv)):
    s += argv[args]
    argv[args] = int(argv[args])
    t += argv[args]
print(s)
print(t)

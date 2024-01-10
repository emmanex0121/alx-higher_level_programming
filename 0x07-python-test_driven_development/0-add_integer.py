#!/usr/bin/python3
# PROGRAM BY PHOENIX
""" module add_integer """


def add_integer(a, b=98):
    """Function That Adds the integer arguments."""

    if type(a) not in (float, int):
        raise TypeError("a must be an integer")
    if type(b) not in (float, int):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b

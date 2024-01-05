#!/usr/bin/python3
# PROGRAM BY PHOENIX

"""
    module add_integer
"""


def add_integer(a, b=98):
    """Function That Adds the integer arguments.

    example in list with integer values:
    >>> [add_integer(n+2, n) for n in range(5)]
    [2, 4, 6, 8, 10]

    Negative int are allowed:
    >>> add_integer(-3, 6)
    3

    floats are casted/converted to int:
    >>> add_integer(3.9, 5)
    8

    >>> add_integer(7, 5.5)
    12

    Strings are not allowed and will raise a TypeError:
    >>> add_integer(-3, "string")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer

    >>> add_integer("h", 14)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer

    """

    if type(a) not in (float, int):
        raise TypeError("a must be an integer")
    if type(b) not in (float, int):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()

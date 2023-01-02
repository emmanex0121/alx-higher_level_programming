#!/usr/bin/python3
# 0-add_integer.py by PHOENIX
"""
This module contains a function that adds two numbers
"""


def add_integer(a, b=98):
    """ Function that adds two integer and/or float values

    Args:
        a: First Number
        b: Second Number

    Returns:
        The sum of the input values

    Raises:
        TypeError: If a or b are not integer or float numbers

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b

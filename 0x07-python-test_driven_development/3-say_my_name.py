#!/usr/bin/python3
# 3-say_my_name.py by Phoenix
"""

This module contains a function that prints name

"""


def say_my_name(first_name, last_name=""):
    """ Function that prints first and last name

        Args:
            first_name: input first name
            last_name: input last name

        Raises:
            TypeError: If first name is not string
                       If last name is not string

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

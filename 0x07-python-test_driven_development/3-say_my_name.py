#!/usr/bin/python3
# Program by Phoenix

"""
    Module say_my_name
"""


def say_my_name(first_name, last_name=""):
    """Function that prints my name

    Test Case first name is int:
    >>> say_my_name(12, "phoenix")
    Traceback (most recent call last):
        ...
    TypeError: first_name must be a string

    Test case last name is int:
    >>> say_my_name("kheed", 16)
    Traceback (most recent call last):
        ...
    TypeError: last_name must be a string

    >>> say_my_name("Phoenix", "Kheed")
    My name is Phoenix Kheed
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")

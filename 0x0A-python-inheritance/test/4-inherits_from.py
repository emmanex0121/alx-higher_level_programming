#!/usr/bin/python3
""" Module that contains function that test direct or indirect inheritance
    of class
"""


def inherits_from(obj, a_class):
    """ Function that returns True if the object is an instance of a class
        that inherited (directly or indirectly) from the specified class
        Otherwise False.
    """
    return (isinstance(obj, a_class) and type(obj) != a_class)

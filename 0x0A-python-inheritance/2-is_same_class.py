#!/usr/bin/python3
# Program By Phoenix
""" Checks if object is an instance of a class """


def is_same_class(obj, a_class):
    """ Returns True if object is exactly an instance of the specified class
        Returns False otherwise
    """
    return (type(obj) == a_class)

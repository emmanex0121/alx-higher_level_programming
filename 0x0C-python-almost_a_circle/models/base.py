#!/usr/bin/python3
# Program By Phoenix
""" Module Base class """


class Base:
    """ Base Class """

    __nb__objects = 0

    def __init__(self, id=None):
        """ Class constructor """

        if id is not None:
            self.id = id
        else:
            Base.__nb__objects += 1
            self.id = Base.__nb__objects

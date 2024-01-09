#!/usr/bin/python3
# Program By Phoenix
"""

This modules contains the classes MYList that inherits from list class

"""


class MyList(list):
    """ A class that inherits from list class """
    def print_sorted(self):
        """ Function that prints sorted list """
        print(sorted(self))

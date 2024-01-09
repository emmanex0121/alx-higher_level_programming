#!/usr/bin/python3
# program By Phoenix
"""Inheris from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class defined inheriting from BaseGeometry"""

    def __init__(self, width, height):
        """ Initializes a new rectangle """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

#!/usr/bin/python3
""" This module Defines a BaseGeometry class """


class BaseGeometry:
    """ Base Geometry Class """

    def area(self):
        """ Raises and Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Rectangle Class inheriting from BaseGeometry Class """

    def __init__(self, width, height):
        """Initializes a new rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

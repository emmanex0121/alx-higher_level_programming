#!/usr/bin/python3
"""Module that Defines Student class"""


class Student:
    """Defines Student class"""
    def __init__(self, first_name, last_name, age):
        """Initializes a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets a dictionary representation of the Student"""
        return self.__dict__
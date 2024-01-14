#!/usr/bin/python3
# Program By Phoenix
""" Module Base class """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries in ([], None):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding="utf-8") as json_file:
            if list_objs is None:
                json.dump([], json_file)
            else:
                list_dicts = []
                for obj in list_objs:
                    list_dicts.append(obj.to_dictionary())
                json.dump(list_dicts, json_file)
                '''json_file.write(Base.to_json_string(list_dicts))'''

    @staticmethod
    def from_json_string(json_string):
        """ Converts Json String Representation to Python Object """
        if json_string in ([], None):
            return []
        return json.loads(json_string)

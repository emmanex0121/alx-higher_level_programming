#!/usr/bin/python3
# Program By Phoenix
""" Module Base class """
import json
import csv
import turtle


class Base:
    """Represent the base model.
    Represents the "base" for all other classes in project 0x0C*.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb__objects = 0

    def __init__(self, id=None):
        """ Class constructor
        Initialize a new Base.
        Args:
            id (int): The identity of the new Base.
        """

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

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if cls.__name__ == "Rectangle":
            dummy_class_inst = cls(4, 4)
        if cls.__name__ == "Square":
            dummy_class_inst = cls(4)

        dummy_class_inst.update(**dictionary)
        return dummy_class_inst

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r', encoding="utf-8") as json_file:
                json_string = json_file.read()
                list_inst_json_str = cls.from_json_string(json_string)

                list_inst_cls = [cls.create(**elem) for elem in
                                 list_inst_json_str]
                return list_inst_cls
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        with open(cls.__name__ + '.csv', 'w', encoding="utf-8") as csv_file:
            if list_objs is None:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                csv_data = csv.DictWriter(csv_file, fieldnames=fieldnames)
                for obj in list_objs:
                    csv_data.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', encoding="utf-8") as csv_file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                csv_data = csv.DictReader(csv_file, fieldnames=fieldnames)

                list_dict_csv = [dict([k, int(v)] for k, v in elem.items())
                                 for elem in csv_data]
                list_dict_csv = [cls.create(**elem) for elem in list_dict_csv]
                return list_dict_csv
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()

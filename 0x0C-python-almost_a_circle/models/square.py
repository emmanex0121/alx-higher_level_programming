#!/usr/bin/python3
# Program By Phoenix
""" module Second Square """
from models.rectangle import Rectangle, run_checks


class Square(Rectangle):
    """ Square class that inherits from Rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        msg = "[{}] ".format(self.__class__.__name__)
        msg = msg + "{:d} {:d}/{:d} - ".format(self.id, self.x, self.y)
        msg = msg + "{:d}".format(self.width)
        return msg

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        run_checks(width=size, height=size)
        self.width = size
        self.height = size
# Or    Rectangle.width = size
# Or    Rectangle.height = size

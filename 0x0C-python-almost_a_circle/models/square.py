#!/usr/bin/python3
# Program By Phoenix
""" module Second Square """
from models.rectangle import Rectangle, run_checks


class Square(Rectangle):
    """ Square class that inherits from Rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        """
            initialises Square (overrides Rectangle init)
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
            Overloading str function
        """
        msg = "[{}] ".format(self.__class__.__name__)
        msg = msg + "({}) {}/{} - ".format(self.id, self.x, self.y)
        msg = msg + "{}".format(self.width)
        return msg

    @property
    def size(self):
        """
            returns the size of the square
        """
        return self.width

    @size.setter
    def size(self, size):
        """
            sets the value of size
        """
        run_checks(width=size, height=size)
        self.width = size
        self.height = size
# Or    Rectangle.width = size
# Or    Rectangle.height = size

    def update(self, *args, **kwargs):
        """
            assigns key/value argument to attributes
            kwargs is skipped if args is not empty
            Args:
                *args -  variable number of no-keyword args
                **kwargs - variable number of keyworded args
        """
        if len(args) < 1:
            for value in kwargs:
                self.__setattr__(value, kwargs[value])
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        """
            Returns the dictionary representation of a Square
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}

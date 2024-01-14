#!/usr/bin/python3
# Program By Phoenix
""" module First Rectangle """
from models.base import Base


def run_checks(**kwargs):
    """
        Function creates valuecheck and Typecheck functions
        And invokes them after
    """

    def type_check(**values):
        """
            Function that takes keyword arguments
            Using Keword arguments dictionary style to seperate arg name
            from its value
            Raises a TypeError if value is not integer
        """
        for value in values:
            if type(values[value]) is not int:
                raise TypeError(f"{value} must be an integer")

    def value_check(**values):
        """
            Function that takes keyword arguments
            Using Keword arguments dictionary style to seperate arg name
            from its value
            Raises a ValueError if value <= 0 for width and height
            Raises a ValueError if value < 0 for x and y
        """
        for value in values:
            if value in ("width", "height"):
                if values[value] <= 0:
                    raise ValueError(f"{value} must be > 0")
            if value in ("x", "y"):
                if values[value] < 0:
                    raise ValueError(f"{value} must be >= 0")

    type_check(**kwargs)
    value_check(**kwargs)


class Rectangle(Base):
    """ Rectangle class inheriting from base class """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        run_checks(width=width, height=height, x=x, y=y)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def area(self):
        """ Public method that returns the area of the traingle """
        return (self.__height * self.__width)

    def display(self):
        """ prints rectangle using # char """
        for i in range(self.__height):
            print("#" * self.__width)

    def update(self, *args, **kwargs):

        if len(args) < 1:
            for key in kwargs:
                self.__setattr__(key, kwargs[key])
        return
# or
# for key, value in kwargs.items():
# self.__setattr__(key, value)

        try:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        except IndexError:
            pass

    def __str__(self):
        msg = "[{}]".format(self.__class__.__name__)
        msg = msg + " ({:d}) {:d}".format(self.id, self.__x)
        msg = msg + "/{:d}".format(self.__y)
        msg = msg + " - {:d}/{:d}".format(self.__width, self.__height)
        return msg

    def to_dictionary(self):
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height, 'width': self.width}

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        run_checks(width=width)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        run_checks(height=height)
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        run_checks(x=x)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        run_checks(y=y)
        self.__y = y

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
        """
            assigns key/value argument to attributes
            kwargs is skipped if args is not empty
            Args:
                *args -  variable number of no-keyword args
                **kwargs - variable number of keyworded args
        """

        if len(args) < 1:
            for key in kwargs:
                self.__setattr__(key, kwargs[key])
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def __str__(self):
        """
            returns a string formart of the rectangle
        """
        msg = "[{}]".format(self.__class__.__name__)
        msg = msg + " ({}) {}".format(self.id, self.__x)
        msg = msg + "/{}".format(self.__y)
        msg = msg + " - {}/{}".format(self.__width, self.__height)
        return msg

    def to_dictionary(self):
        """
            returns the dictionary repr of the class
        """
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height,
                'width': self.width}

    @property
    def width(self):
        """
            getter function for __width
            Returns: width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
            setter function for width.
            Args:
                value (int): value to be set.
        """
        run_checks(width=width)
        self.__width = width

    @property
    def height(self):
        """
            getter function for height
            Returns: height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
            setter function for height
            Args:
                value (int): value to be set.
        """
        run_checks(height=height)
        self.__height = height

    @property
    def x(self):
        """
            getter function for x.
            Returns: x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
            setter function for x.
            Args:
                value (int): value to be set.
        """
        run_checks(x=x)
        self.__x = x

    @property
    def y(self):
        """
            getter function for y
            Returns: y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
            setter function for y
            Args:
                value (int): value to be set.
        """
        run_checks(y=y)
        self.__y = y

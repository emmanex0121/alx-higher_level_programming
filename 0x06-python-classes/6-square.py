#!/usr/bin/python3
# 6-square.py by Phoenix
"""Defines a square """


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing this square class
        Args:
            size: represnets the size of the square defined
            position: where the square is (coordinates)
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieves size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        """set the position of this Square
        Args: value as a tuple of two positive integers
        Raises:
            TypeError: if value is not a tuple or any int in tuple < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrives the Position"""

        return self.__position

    @position.setter
    def position(self, value):
        """set the position of this Square
        Args: value as a tuple of two positive integers
        Raises:
            TypeError: if value is not a tuple or any int in tuple < 0
        """

        if not isinstance(value, (int, int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] <= 0 or value[1] <= 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position == value

    def area(self):
        """
        Calculate area of the square
        Returns: The square of the size
        """

        x = self.__size ** 2
        return x

    def my_print(self):
        """print the square in # """

        if self.__size == 0:
            print()
        else:
            sz = self.__size
            for i in range(sz):
                print("#" * sz)

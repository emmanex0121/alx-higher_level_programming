#!/usr/bin/python3
# 4-square.py by Phoenix
"""Defines a square """


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: represnets the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Retrieves size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

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

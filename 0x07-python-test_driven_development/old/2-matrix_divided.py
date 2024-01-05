#!/usr/bin/python3
"""

This module contains function that divides Matrix elements

"""


def matrix_divided(matrix, div):
    """ Function That divides matrix values

        Args:
            matrix: The matrix
            div: Value to divide the matrix by

        Returns:
            A new divided matrix

        Raises:
            TypeError: If rows size are not equal
                       If matrix is not a list of list of integers/float
                       If div is not a number
                       If the elements of the matrix aren't lists

            ZeroDivisionError: If div is 0

    """
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    msg_size = "Each row of the matrix must have the same size"

    if not isinstance(matrix, list) and not isinstance(matrix, list):
        raise TypeError(msg_type)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    len_e = 0
    for elem in matrix:
        if not isinstance(elem, list):
            raise TypeError(msg_type)
        if len_e != 0 and len(elem) != len_e:
            raise TypeError(msg_size)

        for num in elem:
            if not type(num) in (int, float):
                raise TypeError(msg_type)
        len_e = len(elem)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)

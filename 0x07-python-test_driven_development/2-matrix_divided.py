#!/usr/bin/python3
# Program By Phoenix

"""
    Module matrix_divided

"""

def matrix_divided(matrix, div):
    """ Returns a new matrix of matrix/div """
    new_mat = []

    for i in range(len(matrix)):
        mat = []

        listLenCheck = len(matrix[0])
        if type(div) not in (float, int):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        if len(matrix) > 1:
            if len(matrix[i]) != listLenCheck:
                raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in (float, int):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            mat.append(round(matrix[i][j] / div, 2))
        new_mat += [mat]
    return new_mat

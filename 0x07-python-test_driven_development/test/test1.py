#!/usr/bin/python3

def matrixDivision(arr, div):
    new_mat = []

    for i in range(len(arr)):
        mat = []

        listLenCheck = len(arr[0])
        if type(div) not in (float, int):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        if len(arr) > 1:
            if len(arr[i]) != listLenCheck:
                raise TypeError("Each row of the matrix must \
                        have the same size")
        for j in range(len(arr[i])):
            if type(arr[i][j]) not in (float, int):
                raise TypeError("matrix must be a matrix (list\
                        of lists) of integers/floats")
            mat.append(round(arr[i][j] / div, 2))
        new_mat += [mat]
    return new_mat


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6, 7]]
    print(matrixDivision(matrix, 2))

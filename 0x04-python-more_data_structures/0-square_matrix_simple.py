#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return [[row[i] ** 2 for row in matrix] for i in range(len(matrix))]

    '''
                  OR
    return [list(map(lambda x: x ** 2, row)) for row in matrix]
    '''
    matrix_new = matrix.copy()
    for i in range(len(matrix_new)):
        for row in matrix:
            matrix_new.append(row ** 2)
    return matrix_new

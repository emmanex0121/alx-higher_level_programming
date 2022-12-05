#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    new = []
    for elem in matrix:
        for num in elem:
            if num == elem[-1]:
                print('{:d}'.format(num))
            else:
                print('{:d}'.format(num), end=' ')

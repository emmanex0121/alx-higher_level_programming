#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    new = []
    for elem in matrix:
        print('\n')
        for num in elem:
            print("{:d} ".format(num), end = '')

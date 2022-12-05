#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    new = []
    for elem in matrix:
        print(end = '\n')
        for num in elem:
            print("{:d}".format(num), end = '\n' if num == elem[-1] else ' ')

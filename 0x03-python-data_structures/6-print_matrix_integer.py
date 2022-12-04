#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    new = []
    for elem in matrix:
        for num in elem:
            new.append(num)
    print("{}".format(new))

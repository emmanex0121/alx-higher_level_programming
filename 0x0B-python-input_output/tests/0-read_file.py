#!/usr/bin/python3
""" Module defining reading and writing from file to stdout """


def read_file(filename=""):
    """ Reads a text file and prints to stdout """
    with open(filename, encoding="UTF8") as h:
        file_data = h.read()
    print(file_data, end="")

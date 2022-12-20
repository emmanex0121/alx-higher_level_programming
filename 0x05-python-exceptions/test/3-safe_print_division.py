#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        divAB = a / b
    except ZeroDivisionError:
        divAB = None
    finally:
        print("Inside result: {}".format(divAB))

    return divAB

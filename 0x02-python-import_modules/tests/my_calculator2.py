#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argv = sys.argv

"""Dictionary with keys = operators and values = operators functons"""
ops = {'+': add, '-': sub, '*': mul, '/': div}

if len(argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
else:
    """tests the operator input against the list content"""
    if argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
    else:
        a = int(argv[1])
        b = int(argv[3])
        print("{} {} {} = {}".format(a, argv[2], b, ops[]))

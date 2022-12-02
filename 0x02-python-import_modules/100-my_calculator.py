#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argv = sys.argv

#ops = ['+', '-', '*', '/']
a = int(argv[1])
b = int(argv[3])

if len(argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
else:
    if argv[2] == '+':
        print("{:d} + {:d} = {:d}".format(add(a, b)))
    elif argv[2] == '-':
        print("{:d} - {:d} = {:d}".format(sub(a, b)))
    elif argv[2] == '*':
        print("{:d} * {:d} = {:d}".format(mul(a, b)))
    elif argv[2] == '/':
        print("{:d} / {:d} = {:d}".format(div(a, b)))
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

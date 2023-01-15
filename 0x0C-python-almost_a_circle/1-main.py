#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(11, 4)
    print(r1.id)

    r2 = Rectangle(3, 10, 10, 13)
    print(r2.id)

    r4 = Rectangle(31, 1)
    print(r4.id)

    r3 = Rectangle(14, 2, 0, 0, 12)
    print(r3.id)

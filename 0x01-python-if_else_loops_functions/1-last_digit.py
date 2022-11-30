#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    number = number * -1
    last_num = (number % 10) * -1
    number = number * -1
else:
    last_num = number % 10

if last_num > 5:
    print(f"Last digit of {number} is {last_num} and is greater than 5")
elif last_num == 0:
    print(f"Last digit of {number} is {last_num} and is 0")
elif last_num != 0 and last_num < 6:
    print(f"Last digit of {number} is {last_num} and is less than 5")

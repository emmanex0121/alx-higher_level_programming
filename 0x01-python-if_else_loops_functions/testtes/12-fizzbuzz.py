#!/usr/bin/python3
# Program By Phoenix

for i in range(101):
    if i % 3 == 0:
        print(f"{'Fizz'}", end=' ')
    elif i % 5 == 0:
        print(f"{'Buzz'}", end=' ')
    elif i % 5 == 0 && i % 3 == 0:
        print(f"{'FizzBuzz'}", end=' ')
    else:
        print(f"{i}", end = ' ')

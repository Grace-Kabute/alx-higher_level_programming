#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    print(f"last digit of {number} is {number % 10} and is greater than 0")
if number < 0:
        print(f"last digit of {number} is {abs(number) % 10} and is less than 0")

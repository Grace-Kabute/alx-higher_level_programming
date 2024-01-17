#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last = number % 10
else:
    last = number % -10

if last > 5:
    print(f"last digit of {number:d} is {last} and is greater than 5 and not 0")
elif last < 6 and last != 0:
    print(f"last digit of {number:d} is {last} and is less than 6 and not 0")            
else:
    print(f"the last digit of {number:d} is 0 and is 0")

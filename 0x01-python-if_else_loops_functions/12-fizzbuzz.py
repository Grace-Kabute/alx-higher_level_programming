#!/usr/bin/python3
for i in range (1, 100):
    if i % 3 == 0:
        print("fizz", end=' ')
    elif i % 5 == 0:
        print("buzz", end=' ')
    else:
        print(i, end = ' ')

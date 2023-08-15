#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """prints out even numbers"""
    even = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            even.append(True)
        else:
            even.append(False)

    return even


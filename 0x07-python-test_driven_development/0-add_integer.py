#!/usr/bin/python3
"""adds two integers"""


def add_integer(a, b=98):
    """function adds two intergers
    and returns an integer"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    """cast into intergers"""
    a = int(a)
    b = int(b)
    return a + b

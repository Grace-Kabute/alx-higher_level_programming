#!/usr/bin/python3
"""prints a square with the character #"""


def print_square(size):
    """print a square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size <0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)

#!/usr/bin/python3
"""This a class Square that defines a square"""


class Square:
    """defines a squarenwith private size"""
    def __init__(self, size=0):
        """initialized with size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return int(self.__size) * int(self.__size)

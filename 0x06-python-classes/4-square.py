#!/usr/bin/python3
"""This a class Square that defines a square"""


class Square:
    """defines a squarenwith private size"""
    def __init__(self, size=0):
        """initialized with size"""
        self.size = size

    @property
    def Size(self):
        """retrive size"""
        return self.__size

    @Size.setter
    def size(self, value):
        """set the size value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """area of square"""
        return int(self.__size) * int(self.__size)

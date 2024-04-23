#!/usr/bin/python3
"""This a class Square that defines a square"""
class Square:
    """defines a squarenwith private size"""
    def __init__(self, size=0, position=(0, 0)):
        """initialized with size and position"""
        self.size = size
        self.position = position

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
    
    @property
    def position(self):
        """retrive position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the size value"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value       
    def area(self):
        """area of square"""
        return int(self.__size) * int(self.__size)
    
    def my_print(self):
        """prints the STDOUT"""
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                print("#" * self.size)

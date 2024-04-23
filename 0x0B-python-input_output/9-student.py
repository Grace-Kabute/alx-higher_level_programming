#!/usr/bin/python3
"""defines a studen with class student"""


class Student:
    """defines a class with json"""

    def __init__(self, first_name, last_name, age):
        """initialize fields"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """gets the dictionary fro json"""
        return self.__dict__

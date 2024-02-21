#!/usr/bin/python3
""" class Student that defines a student"""


class Student:
    """defines a class with json"""

    def __init__(self, first_name, last_name, age):
        """initializes fields"""
        self.first = first_name
        self.last = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns attributes"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
     """replaces all attributes of the Student"""
     for k, v in json.items():
        setattr(self, k, v)

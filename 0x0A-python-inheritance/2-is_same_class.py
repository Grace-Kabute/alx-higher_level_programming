#!/usr/bin/python3
"""returns True if the object an instance of a class"""


def is_same_class(obj, a_class):
    """checks instance of a class"""
    if type(obj) == a_class:
        return True
    return False

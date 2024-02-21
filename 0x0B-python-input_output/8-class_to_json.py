#!/usr/bin/python3
"""function that returns the dictionary description"""


def class_to_json(obj):
    """returns the dictionary description"""
    with open("class_to_json", "w", encoding="utf-8") as dic_obj:
        return obj.__dict__

#!/usr/bin/python3
"""writes an object in file in json"""
import json


def save_to_json_file(my_obj, filename):
    """writes in json"""
    with open(filename, mode="w", encoding="utf-8") as json_obj:
        return json.dump(my_obj, json_obj)

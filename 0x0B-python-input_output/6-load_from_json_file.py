#!/usr/bin/python3
""" a function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """write an object from a json file"""
    with open(filename, encoding="utf-8") as object_json:
        return json.load(object_json)

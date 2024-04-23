#!/usr/bin/python3
"""appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends a string at file and returns the number of characters"""
    with open(filename, mode="a", encoding="utf-8") as appends:
        return appends.write(text)

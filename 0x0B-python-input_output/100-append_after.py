#!/usr/bin/python3
"""a function that appends a new string into file"""


def append_after(filename="", search_string="", new_string=""):
    """appends a new string into file"""
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
                with open(filename, "w") as w:
                    w.write(text)

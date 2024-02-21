#!/usr/bin/python3
"""opens, writes and counts charaters in a file"""
def write_file(filename="", text=""):
    """opens and writes in a file"""
    with open(filename, mode="w", encoding = "utf-8") as myCharacters:
        return myCharacters.write(text)

#!/usr/bin/python3
def no_c(my_string):
    """removes letters c and C from the string"""
    new_string = [char for char in my_string if char != "c" and char != "C"]
    return ("".join(new_string))

#!/usr/bin/python3
def max_integer(my_list=[]):
    """finds the largest int"""
    if len(my_list) == 0:
        return None
    else:
        minimum = my_list[0]
        for i in my_list:
            if my_list[i] > minimum:
                max_value = my_list[i]
                return (max_value)

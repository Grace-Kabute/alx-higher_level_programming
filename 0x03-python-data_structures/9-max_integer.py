#!/usr/bin/python3
def max_integer(my_list=[]):
    """finds the largest int"""
    if len(my_list) == 0:
        return None
    else:
        minimum = my_list[0]
        for num in my_list:
            if num > minimum:
                max_value = num
                return max_value

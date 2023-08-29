#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """prints a number of elements of a list"""
    element = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i],end=""))

            element += 1
        except IndexError:
            break
    return (element)

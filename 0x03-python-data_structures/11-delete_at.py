#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """delete one element of list"""
    my_list.remove(my_list[idx])
    if idx < 0 or idx > len(my_list):
        return my_list
    return my_list


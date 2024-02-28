#!/usr/bin/python3
"""base.py"""
class Base:
    """base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """initialize class"""
        if id is not None:
            self.id = id 
        else:
            base.__nb_objects += 1
            self.id = base.__nb_object

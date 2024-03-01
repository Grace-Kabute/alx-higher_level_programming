#!/usr/bin/python3
"""Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square inherits rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """property size"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """add argument"""
        if len(args) and args != 0:
            a = 0
            for arg in args:
                if len(args) == 1:
                    self.id = args[0]
                elif len(args) == 2:
                    self.size = args[1]
                elif len(args) == 3:
                    self.x = args[2]
                elif len(args) == 4:
                    self.y = args[3]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def __str__(self):
        """magic method"""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                                             self.x, self.y, self.size)

    def to_dictionary(self):
        """square dictionary"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
              }

#!/usr/bin/python3
"""
This module contains the Square class, inheriting from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defining the Square class

    Args:
        Rectangle (class): parent class to Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format
              (self.id, self.x, self.y, self.width))

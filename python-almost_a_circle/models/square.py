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
        super().__init__(id, size, size, x, y)
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size <= 0:
            raise ValueError("size must be > 0")

    def __str__(self):
        print("[Square] ({}) {}/{} - {}".format
              (self.id, self.x, self.y, self.width))

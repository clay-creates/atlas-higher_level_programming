#!/usr/bin/python3

"""
This module defines the Square class with the size attribute.
"""


class Square:
    """
    Class Square with a private size attribute
    """
    def __init__(self, size=0):
        """
        __init__ method for the Square class

        Args:
            size (int): size of the Square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        def area(self):
            self.area = size ** 2

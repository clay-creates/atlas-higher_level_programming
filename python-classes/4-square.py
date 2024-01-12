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
        """
        Calculates the area of the Square

        Returns:
            int: Area of the Square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        This is the property getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is the property setter

        Args:
            value (int): size of the Square (public)
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

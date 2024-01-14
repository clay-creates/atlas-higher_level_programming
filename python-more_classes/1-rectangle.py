#!/usr/bin/python3

"""
    This module defines a class: Rectangle
"""


class Rectangle:
    """
    This is the Rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        Initialization module for instances of Rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("with must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @property.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.height = value

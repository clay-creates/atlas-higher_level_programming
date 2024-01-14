#!/usr/bin/python3

"""
This module contains the implementation of the Rectangle class

    Raises:
        TypeError: width type must be an integer
        ValueError: width value must be positive
        TypeError: height type must be an integer
        ValueError: height value must be positive

    Returns:
        Rectangle: returns an instance or instances of Rectangle
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
        """
        Property getter for Rectangle width

        Returns:
            int: returns the class value of __width
        """
        return self.__width

    @property.setter
    def width(self, value):
        """
        Propert setter for Rectangle width

        Args:
            value (int): the value to set rectangle width at

        Raises:
            TypeError: width must be an integer
            ValueError: the value given must be positive
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("with must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Property getter for Rectangle height

        Returns:
            int: returns the class value of __height
        """
        return self.__height

    @property.setter
    def height(self, value):
        """
        Property setter for Rectangle height

        Args:
            value (int): value to set rectangle height at

        Raises:
            TypeError: height must be an integer
            ValueError: value must be positive
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.height = value

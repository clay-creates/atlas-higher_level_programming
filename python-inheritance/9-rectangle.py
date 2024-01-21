#!/usr/bin/python3
"""
This module holds subclass Rectangle inheriting from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Class inheriting from BaseGeometry: Rectangle

    Args:
        BaseGeometry (class): super class to Rectangle
    """
    def __init__(self, width, height):
        """
        Initialization of width and height vars in Rectangle subclass

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Public method that returns rectangle area
        """
        return (self.width * self.height)

    def __str__(self):
        """
        Magic method to print the representation of Rectangle
        """
        print("[Rectangle] {}/{}".format(self.width, self.__height))

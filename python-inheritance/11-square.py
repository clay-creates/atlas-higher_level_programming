#!/usr/bin/python3
"""
This module holds an instance of the Square subclass inheriting fro Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Square class inheriting from Rectangle -> BaseGeometry

    Args:
        Rectangle (class): superclass to Square, subclass of BaseGeometry
    """
    def __init__(self, size):
        """
        Initialization of Square class

        Args:
            size (int): size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates area of Square

        Returns:
            int: size of square
        """
        return (self.__size ** 2)

    def __str__(self):
        """
        Print representation of Square
        """
        print("{}/{}".format(super.__width, super.__height))

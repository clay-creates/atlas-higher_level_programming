#!/usr/bin/python3

"""
This module defines the Square class with the size attribute.
"""


class Square:
    """
    Class Square with a private size attribute
    """
    def __init__(self, size):
        """
        __init__ method for the Square class

        Args:
            size (int): size of the Square
        """
        self.__size = size

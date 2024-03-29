#!/usr/bin/python3

"""
This module defines the Square class with the size attribute.
"""


class Square:
    """
    Class Square with a private size attribute
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        __init__ method for the Square class

        Args:
            size (int): size of the Square
        """
        self.size = size
        self.position = position

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
        Property getter for size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Property setter for size

        Args:
            value (int): size of the Square (public)
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Property getter for position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Property setter for position

        Args:
            value (tuple): tuple containing the position for Square
        """
        err_msg = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple or len(value) != 2:
            raise TypeError(err_msg)
        for i in value:
            if (type(i) is int and i < 0) or type(i) is not int:
                raise TypeError(err_msg)
        else:
            self.__position = value

    def my_print(self):
        """
        This is a method to print our Square using #'s
        """
        if self.__size > 0:
            for _ in range(self.__position[1]):
                print("")
            for _ in range(self.__size):
                for _ in range(self.__position[0]):
                    print(" ", end="")
                for _ in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

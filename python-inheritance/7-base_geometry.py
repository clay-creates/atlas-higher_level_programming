#!/usr/bin/python3
"""
This module creates a new class: BaseGeometry
"""


class BaseGeometry:
    """
    BaseGeometry class
    """
    def area(self):
        """
        Method to calculate area of given geometry

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method to validate values as integer

        Args:
            name (string): name of variable
            value (any): value to check if is int

        Raises:
            TypeError: name must be int
            ValueError: name must be > 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            return True
        
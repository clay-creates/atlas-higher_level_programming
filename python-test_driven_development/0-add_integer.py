#!/usr/bin/python3
"""
This module contains the add_integer method
"""


def add_integer(a, b=98):
    """
    This method adds two integers together. If given a float,
    it will translate them to integers and return the sum.

    Args:
        a (int): first value
        b (int, optional): second value. Defaults to 98.

    Raises:
        TypeError: a value must be an integer
        TypeError: b value must be an integer

    Returns:
        int: sum of two values passed to method
    """

    if type(a) is not [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) is not [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)

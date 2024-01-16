#!/usr/bin/python3

"""
This module defines a method print_square
"""


def print_square(size):
    """
    Prints a square of given size, using "#"

    Args:
        size (int): size of square to print

    Raises:
        TypeError: size must be int
        ValueError: size must be positive
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

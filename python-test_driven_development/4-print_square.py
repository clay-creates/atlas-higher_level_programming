#!/usr/bin/python3

"""
This module defines a method Print_Square
"""


def print_square(size):

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size mist be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

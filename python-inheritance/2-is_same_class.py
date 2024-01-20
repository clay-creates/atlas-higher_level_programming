#!/usr/bin/python3
"""
This module defines the is_same_class method
"""


def is_same_class(obj, a_class):
    """
    Method that checks if an object is an instance of given class

    Args:
        obj (object): object to be checked
        a_class (class): class to see if is instance

    Returns:
        Bool: returns True if is instance, returns False otherwise
    """
    if type(obj) is a_class:
        return True
    else:
        return False

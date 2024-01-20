#!/usr/bin/python3
"""
This module defines the lookup(obj) method
"""


def lookup(obj):
    """
    Method that returns attributes and methods of given object

    Args:
        obj (object): any version of an object

    Returns:
        list: list containing attributes and methods of obj
    """
    return dir(obj)

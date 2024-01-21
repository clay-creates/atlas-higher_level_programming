#!/usr/bin/python3
"""
This module contains the inherits_from method
"""


def inherits_from(obj, a_class):
    """
    This method checks if the object is a subclass of given class

    Args:
        obj (object): object to check
        a_class (class): class to check against

    Returns:
        Bool: return true if is instance, false if not
    """
    if isinstance(super(obj), a_class):
        return True
    else:
        return False

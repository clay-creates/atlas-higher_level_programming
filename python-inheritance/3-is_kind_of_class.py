#!/usr/bin/python3
"""
This method contains the is_kind_of_class method
"""


def is_kind_of_class(obj, a_class):
    """
    Method that checks if object is instance of class/subclass of given class

    Args:
        obj (object): object to be checked
        a_class (class): class to check against

    Returns:
        Bool: returns true if is same class/subclass, false otherwise
    """
    if isinstance (type(obj), a_class):
        return True
    else:
        return False

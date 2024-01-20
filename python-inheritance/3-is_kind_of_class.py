#!/usr/bin/python3
"""
This method contains the is_kind_of_class method
"""


def is_kind_of_class(obj, a_class):
    if isinstance (type(obj), a_class):
        return True
    else:
        return False

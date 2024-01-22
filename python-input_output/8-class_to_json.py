#!/usr/bin/python3
"""
This module implements the class_to_json method
"""


def class_to_json(obj):
    """
    Method that returns dictionary description for json serialization 

    Args:
        obj (_type_): _description_

    Returns:
        _type_: _description_
    """
    return obj.__dict__

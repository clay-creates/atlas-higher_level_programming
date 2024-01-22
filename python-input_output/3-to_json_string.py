#!/usr/bin/python3
"""
This module implements the to_json_string method
"""


import json

def to_json_string(my_obj):
    """
    Method returning JSON representation of object

    Args:
        my_obj (string): object to get json representation

    Returns:
        json: json representation of given object
    """
    return json.dumps(my_obj)

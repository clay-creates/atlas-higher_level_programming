#!/usr/bin/python3
"""
This module implements the from_json_string method
"""


import json

def from_json_string(my_str):
    """
    Method returns an object from a JSOn string

    Args:
        my_str (string): json string to return

    Returns:
        object: object to return
    """
    return json.loads(my_str)
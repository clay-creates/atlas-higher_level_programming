#!/usr/bin/python3
"""
This module implements the load_from_json_file method
"""


import json


def load_from_json_file(filename):
    """
    Method creates an object from a JSON file

    Args:
        my_obj (object): object to be made from json
        filename (string): name of file to get json from
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

#!/usr/bin/python3
"""
This module implements the save_to_json_file method
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Method to write an object to file using json representation

    Args:
        my_obj (object): object to write to file
        filename (string): name of file to write to
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)

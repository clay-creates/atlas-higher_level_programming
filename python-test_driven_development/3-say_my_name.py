#!/usr/bin/python3

"""
This module contains the say_my_name method
"""

def say_my_name(first_name, last_name=""):
    """
    Method to print out both first name and last name given

    Args:
        first_name (string): first name given.
        last_name (str, optional): last name given. Defaults to "".
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

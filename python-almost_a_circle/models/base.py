#!/usr/bin/python3
"""
This module defines the Base class
"""


class Base:
    """
    Base class meant to manage id values of future classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization of Base class

        Args:
            id (int): unique identifier of instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of 'list_dictionaries'

        Args:
            list_dictionaries (list): list of dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return list_dictionaries.__str__

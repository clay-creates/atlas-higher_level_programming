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
        Base.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects

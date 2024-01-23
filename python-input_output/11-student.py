#!/usr/bin/python3
"""
This module implements the Student class
"""


class Student:

    def __init__(self, first_name, last_name, age):
        """
        Initializing Student with firstname, lastname, and age

        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Method to retrieve dictionary representation of Student object

        Args:
            attrs (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}

    def reload_from_json(self, json):
        for key, value in json:
            setattr(self, key, value)

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

    def to_json(self):
        return self.__dict__

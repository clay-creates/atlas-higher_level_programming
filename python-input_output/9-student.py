#1/usr/bin/python3
"""
This module implements the Student class
"""


class Student:

    def __init__(self, first_name, last_name, age):
        if not isinstance((first_name, last_name), str):
            raise TypeError("first_name and last_name must be a string")
        if not isinstance(age, int):
            raise TypeError("age must be an integer")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

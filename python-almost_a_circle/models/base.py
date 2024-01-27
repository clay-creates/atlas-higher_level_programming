#!/usr/bin/python3
"""
This module defines the Base class
"""
import json, os


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
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of 'list_objs' to a file

        Args:
            list_objs (list): list of instances who inherits from Base
        """
        filename = "{}.json".format(cls.__name__)

        if not list_objs:
            list_objs = []

        list_objs = [object.to_dictionary() for object in list_objs]
        json_string = cls.to_json_string(list_objs)

        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of JSON string representation 'json_string'

        Args:
            json_string (string): string representing a list of dicts

        Returns:
            _type_: _description_
        """
        if not json_string:
            return []

        list_of_dicts = json.loads(json_string)
        return list_of_dicts

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            new_inst = cls(1, 1)
        if cls.__name__ == "Square":
            new_inst = cls(1)
        new_inst.update(**dictionary)
        return new_inst

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """
        filename = "{}.json".format(cls.__name__)

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as file:
            json_string = file.read()

        list_of_dicts = cls.from_json_string(json_string)
        list_of_instances = [cls.create(**dictionary) 
                             for dictionary in list_of_dicts]

        return list_of_instances

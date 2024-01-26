#!/usr/bin/python3
"""
This module contains the Square class, inheriting from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defining the Square class

    Args:
        Rectangle (class): parent class to Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        id = self.id
        x = self.x
        y = self.y
        width = self.width
        return ("[Square] ({}) {}/{} - {}".format(id, x, y, width))

    @property
    def size(self):
        """
        Getter for size

        Returns:
            int: size of square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size

        Args:
            value (int): value to set size to
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Function to update Square values
        """
        attributes = ['id', 'size', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs:
            for attr, value in kwargs.items():
                if attr in attributes:
                    setattr(self, attr, value)

    def to_dictionary(self):
        """
        Funtion to put Square attributes in dictionary
        """
        attr_dict = {}
        attr_dict['id'] = getattr(self, 'id')
        attr_dict['size'] = getattr(self, 'size')
        attr_dict['x'] = getattr(self, 'x')
        attr_dict['y'] = getattr(self, 'y')

        return attr_dict

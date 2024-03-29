#!/usr/bin/python3
"""
This module contains the Rectangle class, inheriting from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Implementation of Rectangle class

    Args:
        Base (class): parent class to Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialization of Rectangle class

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int, optional): horizontal position. Defaults to 0.
            y (int, optional): vertical position. Defaults to 0.
            id (int, optional): id number of instance. Defaults to None.
        """
        super().__init__(id)
        if width is not None:
            if not isinstance(width, int):
                raise TypeError("width must be an integer")
            elif width <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = width

        if height is not None:
            if not isinstance(height, int):
                raise TypeError("height must be an integer")
            elif height <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    @property
    def width(self):
        """
        Getter for width attribute

        Returns:
            int: returns width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width attribute

        Args:
            value (int): value to set width to

        Raises:
            TypeError: must be int
            ValueError: must be > 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter for height attribute

        Returns:
            int: returns height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height attribute

        Args:
            value (int): value to set height to

        Raises:
            TypeError: must be int
            ValueError: must be > 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        Getter for x attribute

        Returns:
            int: horizontal position on axis
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x attribute

        Args:
            value (int): value to set x at

        Raises:
            TypeError: must be int
            ValueError: must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        Getter for y attribute

        Returns:
            int: vertical position on axis
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y attribute

        Args:
            value (int): value to set y at

        Raises:
            TypeError: must be int
            ValueError: must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Funtion to get area of rectangle

        Returns:
            int: return area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Funtion to display representation of rectangle
        """
        for _ in range(self.y):
            print("")
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
              (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        Function to update values of attribute
        """
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs:
            for attr, value in kwargs.items():
                if attr in attributes:
                    setattr(self, attr, value)

    def to_dictionary(self):
        """
        Funtion to put Rectangle attributes in dictionary
        """
        attr_dict = {}
        attr_dict['id'] = getattr(self, 'id')
        attr_dict['width'] = getattr(self, 'width')
        attr_dict['height'] = getattr(self, 'height')
        attr_dict['x'] = getattr(self, 'x')
        attr_dict['y'] = getattr(self, 'y')

        return attr_dict

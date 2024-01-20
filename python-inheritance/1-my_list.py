#!/usr/bin/python3
"""
Module with MyList subclass inheriting from built-in list class
"""


class MyList(list):
    """
    Subclass inheriting from list built in class

    Args:
        list (class): superclass that our class inherits from
    """

    def print_sorted(self):
        """
        Method to print sorted list
        """
        print(sorted(self))

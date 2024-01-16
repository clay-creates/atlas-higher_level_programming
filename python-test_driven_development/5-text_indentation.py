#!/usr/bin/python3

"""
This module contains implementation of the text_indentation method
"""


def text_indentation(text):
    """
    This method prints two newlines after these characters: ['.', '?', ':']

    Args:
        text (str): text to be printed out and indented

    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        if char in ['.', '?', ':']:
            print("char\n")
        print(char, end="")

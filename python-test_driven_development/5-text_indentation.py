#!/usr/bin/python3

"""
This module contains implementation of the text_indentation method
"""

def text_indentation(text):

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for char in range(text):
        if char == ['.', '?', ':']:
            print("\n")
        print(char, end="")
        
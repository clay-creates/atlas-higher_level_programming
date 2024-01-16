#!/usr/bin/python3

"""
This module contains implementation of the text_indentation method
"""

def text_indentation(text):

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for char in len(range(text)):
        if text[char] == ['.', '?', ':']:
            print("\n")
        print(char, end="")
        
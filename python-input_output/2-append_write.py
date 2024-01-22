#!/usr/bin/python3
"""
This module implements the append_write method
"""


def append_write(filename="", text=""):
    """
    Method appending to given file, return num of chars appended

    Args:
        filename (str, optional): name of file to append to. Defaults to "".
        text (str, optional): text to append. Defaults to "".

    Returns:
        int: num of chars appended
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)

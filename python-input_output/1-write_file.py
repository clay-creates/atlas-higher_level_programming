#!/usr/bin/python3
"""
This module contains implementation of write_file method
"""


def write_file(filename="", text=""):
    """
    Method writes to given file and gives number of characters written

    Args:
        filename (str, optional): name of file to write to. Defaults to "".
        text (str, optional): text to write. Defaults to "".

    Returns:
        int: return number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)
        return len(text)
        
#!/usr/bin/python3
"""
This module defines the read_file method
"""


def read_file(filename=""):
    """
    Method reads a file and prints it to stdout

    Args:
        filename (str, optional): UTF8 file. Defaults to "".
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")

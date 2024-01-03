#!/usr/bin/python3

def uppercase(str):

    for char in str:
        chr(ord(char) - 32)
    return str
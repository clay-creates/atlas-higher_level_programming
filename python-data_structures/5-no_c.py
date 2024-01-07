#!/usr/bin/python3

def no_c(my_string):
    for char in my_string:
        if char == 'c' or char == 'C':
            my_string[char] = ''

    return my_string

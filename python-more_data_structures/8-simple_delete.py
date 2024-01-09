#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):

    if key is None:
        return a_dictionary

    for i in a_dictionary:
        if a_dictionary[i] == key:
            del(a_dictionary[i])
        else:
            a_dictionary += key

    return a_dictionary

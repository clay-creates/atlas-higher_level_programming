#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    sort_items = sorted(a_dictionary.keys())
    for i in sort_items:
        print("{}: {}".format(i, a_dictionary[i]))

#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    sort_items = sorted(a_dictionary.items())
    sorted_dict = dict(sort_items)
    print("{}".format(sorted_dict))

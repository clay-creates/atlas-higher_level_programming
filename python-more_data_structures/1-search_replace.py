#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    elif search is None or replace is None:
        return my_list

    new_list = my_list

    for element in my_list:
        if element == search:
            new_list[element] = replace

    return new_list

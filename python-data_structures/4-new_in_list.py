#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list

    new = my_list[:]

    for i in new:
        if i == idx:
            new[i] = element

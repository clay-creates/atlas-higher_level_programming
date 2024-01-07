#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new = None
    
    if idx < 0:
        new = my_list
        return new
    elif idx > len(range(my_list)):
        new = my_list
        return new
    
    new = my_list
    
    for i in range(new):
        if i == idx:
            new[i] = element

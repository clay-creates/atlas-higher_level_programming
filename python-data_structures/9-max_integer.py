#!/usr/bin/python3

def max_integer(my_list=[]):
    big_int = 0
    
    if my_list is None:
        return None
    
    for i in range(my_list):
        if i > big_int:
            big_int = i

    return big_int

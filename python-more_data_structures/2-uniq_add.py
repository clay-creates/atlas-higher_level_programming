#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_nums = set(my_list)
    sum = 1
    for i in uniq_nums:
        sum *= i

    return sum

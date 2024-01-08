#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_sum = set(my_list)

    for i in uniq_sum:
        uniq_sum *= i

    return uniq_sum

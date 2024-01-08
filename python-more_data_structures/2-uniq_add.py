#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_sum = []

    for i in set(my_list):
        uniq_sum += i

    return uniq_sum

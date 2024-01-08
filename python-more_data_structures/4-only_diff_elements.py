#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    set1 = set(set_1)
    set2 = set(set_2)

    diff = [i for i in set1 if i not in set2]
    return diff

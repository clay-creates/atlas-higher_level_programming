#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    a_sum = 0
    b_sum = 0

    for i in tuple_a:
        a_sum += i

    for i in tuple_b:
        b_sum += i

    new_tuple = (a_sum, b_sum)
    return new_tuple

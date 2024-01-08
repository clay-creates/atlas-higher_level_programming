#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a_sum = tuple_a + (0, 0)
    b_sum = tuple_b + (0, 0)

    new_a = a_sum[0] + b_sum[0]
    new_b = a_sum[1] + b_sum[1]

    return (new_a, new_b)

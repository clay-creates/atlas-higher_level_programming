#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a_sum = sum(tuple_a[:2])
    b_sum = sum(tuple_b[:2])

    return (a_sum, b_sum)

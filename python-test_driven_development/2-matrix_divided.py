#!/usr/bin/python3

"""
This module contains a method to divide all elements of a given matrix.    
"""

def matrix_divided(matrix, div):
    """
    This is a method for dividing a given matrix by a given divisor

    Args:
        matrix (list): list of lists passed to method
        div (int): the value to divide each element of matrix by

    Raises:
        TypeError: div argument must be a number
        ZeroDivisionError: cannot divide by zero
        TypeError: matrix must be a matrix
        TypeError: matrix must be a matrix
        TypeError: rows of matrix must be the same size

    Return: returns a new_matrix with the divided values, rounded to two decimals
    """

    new_matrix = [[]]

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(matrix, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        for i in range(len(row)):
            new_matrix += round(matrix[i] / div, 2)

    return new_matrix

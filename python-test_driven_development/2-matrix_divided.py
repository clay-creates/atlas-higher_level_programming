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

    #Check if div is a number, check if number is zero
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    #Check if matrix is a list of lists
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix)):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    #Check if rows in matrix are the same size
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [
        [round(i / div, 2) for i in row] for row in matrix
    ]
    
    return new_matrix

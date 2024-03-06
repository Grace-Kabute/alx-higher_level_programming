#!/usr/bin/python3
"""Divides matrix"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix"""
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if all rows have the same length
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check if div is a non-zero number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div
    divided_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return divided_matrix

#!/usr/bin/python3
"""defines function divide matrix"""


def matrix_divided(matrix, div):
    """divides matrix by scalar integer"""
    len_rows = 0
    len_cols = 0
    matrix_result = []
    
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not type(div) in (int, float):
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")

    # Iterate over rows in the matrix
    for row in matrix:
        len_rows += 1

        # Check if each row is a list
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        # Iterate over elements in the row
        for elem in row:
            # Check if each element is a number
            if not type(elem) in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        # Check if all rows have the same length
        if len_rows == 1:
            len_cols = len(row)
        elif len(row) != len_cols:
            raise TypeError("Each row of the matrix must have the same size")

        # Perform division and store the result in the new matrix
        matrix_result.append([round(elem/div, 2) for elem in row])

    # Check if the matrix is not empty
    if len_rows == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")


    return matrix_result


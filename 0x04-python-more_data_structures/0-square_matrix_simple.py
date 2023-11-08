#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix2 = []
    square = lambda x : x ** 2

    for i in matrix:
        matrix2.append(list(map(square, i)))

    return matrix2


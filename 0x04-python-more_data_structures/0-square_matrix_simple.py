#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix2 = []
    for i in matrix:
        matrix2.append(list(map(lambda x: x ** 2, i)))

    return matrix2

#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [[it[i]**2 for i in range(len(it))] for it in matrix]

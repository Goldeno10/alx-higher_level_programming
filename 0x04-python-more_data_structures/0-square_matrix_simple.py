#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr_mtx = [[it[i]**2 for i in range(len(it))] for it in matrix]
    return sqr_mtx

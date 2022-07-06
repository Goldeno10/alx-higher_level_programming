#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr_mtx = [it[i]**2 for it in matrix for i in range(len(it))]
    return sqr_mtx

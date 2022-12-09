#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    result = map(lambda x:  list(map(lambda y: y * y, x)), matrix_cpy)
    return list(result)

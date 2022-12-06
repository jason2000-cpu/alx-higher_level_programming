#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    two_D_squared_matrix = []
    for i in range(len(matrix)):
        j = 0
        squared_matrix = []
        while j < len(matrix[i]):
            squared_matrix.append(matrix[i][j] * matrix[i][j])
            j += 1
        two_D_squared_matrix.append(squared_matrix)

    return two_D_squared_matrix

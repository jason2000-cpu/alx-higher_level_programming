#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    matrix_cpy =  matrix.copy()
    result = map(lambda x:  list( map(lambda y: y * y, x)), matrix_cpy)
    return list(result)
    
    
    
    
    
    

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


new_matrix = square_matrix_map(matrix)
print(new_matrix)
print(matrix)
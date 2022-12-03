#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        j = 0
        while j < len(matrix[i]):
            
            if i == len(matrix)-1:
                 print("{:d}".format(matrix[i][j]), end=" ")
                 j +=1

            else:
                print("{:d}".format(matrix[i][j]))
                j +=1




matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
    
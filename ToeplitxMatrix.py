'''You are given a square matrix of n x n size. Your task is to write a
 Python function that indicates whether the matrix is a Toeplitz matrix.

In a Toeplitz matrix, each descending diagonal (from left to right) is 
constant. That is, elements in each descending diagonal are the exact same.

For example, if the given matrix is:
6 7 8
4 6 7
1 4 6

Your function should return True because all diagonals from top-left to bottom-right are:
[1], [4, 4], [6, 6, 6], [7, 7], [8]
'''

from typing import List

def is_toeplitz(matrix: List[List[int]]) -> bool:
   # TODO: implement
    if not matrix or len(matrix) == 1:
        return True
    for i in range(len(matrix)-1):
        for j in range(len(matrix)-1):
            print(matrix[i][j], matrix[i+1][j+1])
            if matrix[i][j] != matrix[i+1][j+1]:
                return False
    return True

matrix = [[4, 4, 4, 4], 
         [1, 4, 4, 4], 
         [4, 1, 4, 4], 
         [4, 4, 0, 4]]
print(is_toeplitz(matrix))

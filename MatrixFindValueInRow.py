'''You are given a matrix of integers where every row and column 
are sorted in ascending order. Your task is to find the row that 
contains a specific target value. If the target value doesn't 
exist, return None.

The expected time complexity is 
O(n+m), where n is the number of rows and 
m is the number of columns.
'''

def find_row_with_target(matrix: list[list[int]], target: int) -> int | None:
    # TODO: Implement the solution here
    if not matrix or not matrix[0]:
        return None
    rows = len(matrix)
    cols = len(matrix[0])
    row = 0
    col = cols - 1
    while row < rows and col >= 0:
        if matrix[row][col] == target:
            print(row)
            return row
        if matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    return None
matrix = [
            [1, 4, 7, 11],
            [2, 5, 8, 12],
            [3, 6, 9, 16]
        ]
target = 9

find_row_with_target(matrix, target)
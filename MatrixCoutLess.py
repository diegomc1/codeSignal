'''You're given a matrix where each row is sorted in ascending order. 
The columns are also sorted in ascending order. This creates a special 
pattern where the values in the matrix increase as you move right or 
down but decrease as you move left or up.

Your task is to write a Python function that counts the number of 
integers in the matrix that are smaller than the given target. 
The function should return this count as an integer.

The expected complexity is 
O(n+m), where 
n is the number of rows and 
m is the number of columns in the matrix.

For example, given a matrix:
[
  [1, 2, 3, 4],
  [2, 3, 4, 5],
  [3, 4, 5, 6],
  [4, 5, 6, 7]
]

and a target of 5, the function count_less_than(matrix, 5) 
should return 10 because there are 10 numbers in the matrix 
that are less than 5.
'''

def count_less_than(matrix, target):
    # TODO: Your code goes here. Remember that the matrix is sorted row-wise and column-wise!
    if not matrix or not matrix[0]:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    # Start at the top-right corner
    row = 0
    col = cols - 1
    while row < rows and col >= 0:
        if matrix[row][col] < target:
            # All elements in the current row up to col are less than target
            count += col + 1
            # Move to the next row
            row += 1
        else:
            # Move to the previous column
            col -= 1
    return count
matrix = [[1]]
target = 1
print(count_less_than(matrix, target))
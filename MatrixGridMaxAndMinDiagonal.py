'''Given a square matrix grid of integers, your task is to find 
the minimum and maximum values at the secondary diagonal. The 
secondary diagonal starts at the top right corner and ends at 
the bottom left corner.

Return a list of two elements where the first element is the 
minimum value, and the second is the maximum value that you 
have found in the diagonal. If the square matrix is empty, 
return [None, None].

The time complexity of the solution should not exceed 
O(n), where n is the length of the row (or column) in the grid.'''

def solution(grid):
    # TODO: implement the solution here
    if not grid or not grid[0]:
        return [None,None]
    rows = len(grid)
    cols = len(grid[0])
    # Start top right
    row = 0
    col = cols - 1
    # Set values of the top right to min and max
    min_val = grid[0][col]
    max_val = grid[0][col]
    # Traverse with secondary diagonal (top right to bottom left)
    for i in range(rows):
        # Compare and update min and max values
        if grid[i][col] >= max_val:
            max_val = grid[i][col]
        if grid[i][col] <= min_val:
            min_val = grid[i][col]
        # col - 1 to traverse secondary diagonal
        col -= 1
    return([min_val, max_val])

grid = [[-5, -1, -9, -11], 
        [-2, -4, -8, -10], 
        [-13, -3, -6, -7], 
        [-15, -14, -12, -16]]
solution(grid)

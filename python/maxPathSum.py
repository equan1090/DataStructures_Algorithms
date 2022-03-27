'''
max path sum
Write a function, max_path_sum, that takes in a grid as an argument.
The function should return the maximum sum possible by traveling a path from the top-left corner
 to the bottom-right corner. You may only travel through the grid by moving down or right.

You can assume that all numbers are non-negative.
'''


def max_path_sum(grid):
    return _max_path_sum(grid, 0, 0, {})


def _max_path_sum(grid, row, col, memo):
    pos = (row, col)
    if pos in memo:
        return memo[pos]

    if row == len(grid) or col == len(grid[0]):
        return 0

    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        return grid[row][col]

    downPath = _max_path_sum(grid, row + 1, col, memo)
    rightPath = _max_path_sum(grid, row, col + 1, memo)

    memo[pos] = grid[row][col] + max(downPath, rightPath)
    return memo[pos]

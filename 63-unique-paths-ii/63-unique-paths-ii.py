class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        return self.dfs(obstacleGrid, 0, 0, {})
        
    def dfs(self, grid, row, col, memo):
        pos = (row, col)
        if pos in memo:
            return memo[pos]
        
        if row == len(grid) or col == len(grid[0]) or grid[row][col] == 1:
            return 0
        
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return 1
        
        
        
        down = self.dfs(grid, row + 1, col, memo)
        right = self.dfs(grid, row, col + 1, memo)
        
        memo[pos] = down + right
        return memo[pos]
        
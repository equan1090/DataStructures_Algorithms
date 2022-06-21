class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        longest = 0
        memo = {}
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                attempt = self.dfs(matrix, row, col, float('-inf'), memo)
                longest = max(attempt, longest)
        return longest
        
        
        
    def dfs(self, matrix, r, c, prev, memo):
        key = (r, c)
        rowBounds = 0 <= r < len(matrix)
        colBounds = 0 <= c < len(matrix[0])

        if not rowBounds or not colBounds:
            return 0
        
        if matrix[r][c] <= prev:
            return 0
        if key in memo:
            return memo[key]
        
        res = 1
        res = max(res, 1 + self.dfs(matrix, r + 1, c, matrix[r][c], memo))
        res = max(res, 1 + self.dfs(matrix, r - 1, c, matrix[r][c], memo))
        res = max(res, 1 + self.dfs(matrix, r, c + 1, matrix[r][c], memo))
        res = max(res, 1 + self.dfs(matrix, r, c - 1, matrix[r][c], memo))
        
        memo[key] = res
        return memo[key]
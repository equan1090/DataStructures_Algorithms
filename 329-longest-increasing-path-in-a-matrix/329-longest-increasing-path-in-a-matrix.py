class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        longest = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                attempt = self.dfs(matrix, r, c, float('-inf'), memo)
                longest = max(longest, attempt)
        return longest
        
        
    def dfs(self, matrix, r, c, prev, memo):
        key = (r, c)
        rowbounds = 0 <= r < len(matrix)
        colbounds = 0 <= c < len(matrix[0])
        
        
        if not rowbounds or not colbounds:
            return 0
        
        if matrix[r][c] <= prev:
            return 0
        if key in memo:
            return memo[key]
        res = 1
        res = max(res, 1 +self.dfs(matrix, r + 1, c, matrix[r][c], memo))
        res = max(res, 1 +self.dfs(matrix, r - 1, c, matrix[r][c], memo))
        res = max(res, 1 +self.dfs(matrix, r, c + 1, matrix[r][c], memo))
        res = max(res, 1 +self.dfs(matrix, r, c - 1, matrix[r][c], memo))
        
        memo[key] = res
        return memo[key]
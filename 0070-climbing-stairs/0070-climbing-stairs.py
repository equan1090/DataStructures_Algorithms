class Solution:
    def climbStairs(self, n: int) -> int:
        return self.dfs(n, {0: 1, 1: 1})
        
    def dfs(self, n, memo):
        if n in memo:
            return memo[n]
        
        
        memo[n] = self.dfs(n - 1, memo) + self.dfs(n - 2, memo)
        return memo[n]
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        ans = self.dfs(coins, amount, {})
        return ans if ans != float('inf') else -1
        
    def dfs(self, coins, amount, memo):
        if amount in memo:
            return memo[amount]
        
        if amount == 0:
            return 0
        
        if amount < 0:
            return float('inf')
        
        res = float('inf')
        for coin in coins:
            attempt = 1 + self.dfs(coins, amount - coin, memo)
            res = min(res, attempt)
        
        memo[amount] = res
        return memo[amount]
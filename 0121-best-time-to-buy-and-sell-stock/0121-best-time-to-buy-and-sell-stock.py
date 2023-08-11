class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            if profit < 0:
                profit = 0
                l = r
            res = max(profit, res)
        return res
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        
        for r in range(len(prices)):
            curProfit = prices[r] - prices[l]
            if curProfit < 0:
                
                l = r
            res = max(res, curProfit)
        return res
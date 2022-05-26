class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        res = 0
        
        for r in range(len(prices)):
            curPrice = prices[r] - prices[l]
            if curPrice < 0:
                curPrice = 0
                l = r
            res = max(curPrice, res)
        return res
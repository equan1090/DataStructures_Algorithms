class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        for r in range(len(prices)):
            curPrice = prices[r] - prices[l]
            if curPrice < 0:
                curPrice = 0
                l = r
            res = max(res, curPrice)
        return res
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProfit = 0
        while r < len(prices):
            curProfit = prices[r] - prices[l]
            if curProfit < 0:
                curProfit = 0
                l = r
            maxProfit = max(maxProfit, curProfit)
            r += 1
        return maxProfit
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = nums[0]
        curSum = 0
        for i in range(len(nums)):
            if curSum < 0:
                curSum = 0
            curSum += nums[i]
            res = max(res, curSum)

        return res
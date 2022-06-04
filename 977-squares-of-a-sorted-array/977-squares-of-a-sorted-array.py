class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        res = [0] * len(nums)
        
        for i in range(len(nums) -1, -1, -1):
            leftValue = abs(nums[l])
            rightValue = abs(nums[r])
            if leftValue > rightValue:
                res[i] = leftValue**2
                l += 1
            else:
                res[i] = rightValue**2
                r -= 1
        return res
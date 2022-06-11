class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        return self.dfs(nums, target, 0, 0, {})
    
    def dfs(self, nums, target, i, curSum, memo):
        key = (i, curSum)
        if key in memo:
            return memo[key]
        
        if i == len(nums):
            return 1 if curSum == target else 0
        
        add = self.dfs(nums, target, i+1, curSum + nums[i], memo)
        subtract = self.dfs(nums, target, i+1, curSum - nums[i], memo)
        
        memo[key] = add + subtract
        return memo[key]
    
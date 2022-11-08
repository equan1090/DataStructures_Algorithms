class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        return self.dfs(nums, [], [])
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return 
        
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)
        return res
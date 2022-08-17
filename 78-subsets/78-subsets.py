class Solution:
    def subsets(self, nums):
        res = []
        self.generateSubsets(nums, res, [], 0)
        return res
    def generateSubsets(self, nums, res, curr, index):
        res.append(list(curr))
        for i in range(index, len(nums)):
            curr.append(nums[i])
            self.generateSubsets(nums, res, curr, i + 1)
            curr.pop()
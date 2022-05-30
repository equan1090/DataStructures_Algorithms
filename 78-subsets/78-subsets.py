class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        first = nums[0]
        no_first = self.subsets(nums[1:])
        path = []
        
        for sub in no_first:
            path.append([first, *sub])
        return no_first + path
    
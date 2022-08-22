class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        res = 0
        for i in setNums:
            if i-1 in setNums:
                continue
            
            current = 0
            while current + i in setNums:
                current += 1
            res = max(res, current)
        return res
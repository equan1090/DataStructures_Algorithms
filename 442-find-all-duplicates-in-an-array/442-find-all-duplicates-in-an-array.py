class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            idx = abs(num)
            if nums[idx-1] < 0:
                res.append(idx)
            else:
                nums[idx-1] = -nums[idx-1]
        return res
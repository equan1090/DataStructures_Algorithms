class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in pairs:
                return [pairs[compliment], i]
            pairs[num] = i
        return []
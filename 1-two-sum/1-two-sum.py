class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for idx, num in enumerate(nums):
            compliment = target - num
            if compliment in pairs:
                return [idx, pairs[compliment]]
            pairs[num] = idx
        return -1
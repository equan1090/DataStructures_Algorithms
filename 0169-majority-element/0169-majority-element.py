class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
            
            if freq[num] >= (len(nums)// 2) + 1:
                return num
        
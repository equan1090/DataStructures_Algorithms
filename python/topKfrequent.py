'''
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        # 1: 3, 2: 2, 3: 1
        for val, idx in freq.items():
            bucket[idx].append(val)

        res = []
        for i in reversed(range(len(bucket))):
            for val in bucket[i]:
                res.append(val)
                if len(res) == k:
                    return res

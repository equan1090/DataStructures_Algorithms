class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket = [[][3][2][1][][][]]
        bucket = [[] for i in range(len(nums) + 1)]
        freq = {}
        
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        
        # freq = {1: 3, 2: 2, 3: 1}
        for val, idx in freq.items():
            bucket[idx].append(val)
        
        res = []
        
        for i in range(len(bucket) - 1, - 1, -1):
            for val in bucket[i]:
                res.append(val)
                if len(res) == k:
                    return res
        return []
            
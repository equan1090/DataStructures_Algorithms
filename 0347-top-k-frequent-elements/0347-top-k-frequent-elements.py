class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        count = {}
        res = []
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for val, idx in count.items():
            bucket[idx].append(val)
        
        for i in range(len(bucket) -1, -1, -1):
            for val in bucket[i]:
                res.append(val)
                if len(res) == k:
                    return res
        
        
        
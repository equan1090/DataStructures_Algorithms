class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        
        
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        for val, idx in freq.items():
            bucket[idx].append(val)
        
        #[[][3][2][1][][][]]
        
        res = []
        for i in range(len(bucket)-1, -1, -1):
            for val in bucket[i]:
                res.append(val)
                if len(res) == k:
                    return res
        return -1
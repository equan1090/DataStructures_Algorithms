class Solution:
    def minDeletions(self, s: str) -> int:
        count = {}
        res = 0
        for c in s:
            count[c] = 1 + count.get(c, 0)
        
        countSet = set()
        for char, val in count.items():
            while val > 0 and val in countSet:
                val -= 1
                
                res += 1
            countSet.add(val)
        return res
class Solution:
    def minDeletions(self, s: str) -> int:
        freq = {}
        for c in s:
            freq[c] = 1 + freq.get(c, 0)
        res = 0
        countSet = set()
        for char, count in freq.items():
            while count > 0 and count in countSet:
                count -= 1
                res += 1
            countSet.add(count)
        return res
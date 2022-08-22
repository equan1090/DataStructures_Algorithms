class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return self.counter(s) == self.counter(t)
        
    def counter(self, s):
        freq = {}
        for c in s:
            freq[c] = 1 + freq.get(c, 0)
        return freq
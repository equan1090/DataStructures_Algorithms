class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.compare(s) == self.compare(t)
        
    def compare(self, s):
        count = {}
        for c in s:
            count[c] = 1 + count.get(c, 0)
        return count
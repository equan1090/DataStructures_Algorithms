class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return self.check(s) == self.check(t)
        
    def check(self, s):
        count = {}
        
        for c in s:
            if c not in count:
                count[c] = 0
            count[c] += 1
        return count
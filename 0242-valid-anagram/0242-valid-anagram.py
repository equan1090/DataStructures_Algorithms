class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.counter(s) == self.counter(t)
    
    def counter(self, word):
        count = {}
        for c in word:
            count[c] = 1 + count.get(c, 0)
        return count
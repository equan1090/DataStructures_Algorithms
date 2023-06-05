class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return self.anagram(s) == self.anagram(t)
        
        
    def anagram(self, word):
        count = {}
        for char in word:
            count[char] = 1 + count.get(char, 0)
        return count
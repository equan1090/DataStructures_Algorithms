class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        d1 = {i:0 for i in range(26)}
        d2 = {i:0 for i in range(26)}
        
        for i in range(len(s1)):
            d1[ord(s1[i]) - ord('a')] += 1
            d2[ord(s2[i]) - ord('a')] += 1
            
        start = 0
        end = len(s1) - 1
        
        while end < len(s2):
            if d1 == d2:
                return True
            
            d2[ord(s2[start]) - ord('a')] -= 1
            start += 1
            end += 1
            if end < len(s2):
                
                d2[ord(s2[end]) - ord('a')] += 1
        return False
            
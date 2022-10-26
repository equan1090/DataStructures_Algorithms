class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        for c in s:
            freq[c] = 1 + freq.get(c, 0)
        
        odd = False
        res = 0
        
        for k,v in freq.items():
            if v % 2 == 0:
                res += v
            else:
                res += v-1
                odd = True
        
        if odd:
            res += 1
            
        return res
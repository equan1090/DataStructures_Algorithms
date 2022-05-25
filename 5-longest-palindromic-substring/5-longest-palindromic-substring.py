class Solution:
    def longestPalindrome(self, s: str) -> str:

        start = 0
        maxLen = 0
        i = 0

        while i < len(s):
            
            l = i
            r = i
            i = r + 1
            while r < len(s) - 1 and s[r] == s[r+1]:
                r += 1
            
            while r < len(s) - 1 and l > 0 and s[r+1] == s[l-1]:
                l -= 1
                r += 1
            if maxLen < r - l + 1:
                start = l
                maxLen = r - l + 1
        return s[start: start + maxLen]
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        tCount = {}
        
        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)
        
        have = 0
        need = len(tCount)
        l = 0
        resLen = float('inf')
        res = [-1, -1]
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in tCount and window[c] == tCount[c]:
                have += 1
            
            while have == need:
                char = s[l]
                
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                
                window[char] -= 1
                l += 1
                if char in tCount and window[char] < tCount[char]:
                    have -= 1
        
        l, r = res
        return s[l:r+1]
                    
            
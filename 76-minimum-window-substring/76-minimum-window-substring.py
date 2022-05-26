class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''
        
        l = 0
        resLen = float('inf')
        res = [-1, -1]
        tCount = {}
        window = {}

        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)
            
        have, need = 0, len(tCount)
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            if c in tCount and window[c] == tCount[c]:
                have += 1
                
            while have == need:
                
                
                if (r - l + 1) < resLen:
                    resLen = (r - l + 1)
                    res = [l, r]
                
                window[s[l]] -= 1
                if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1]
                
            

            
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         l = 0
#         resLen = float('inf')
#         res = [-1, -1]
#         tCount = {}
#         window = {}
#         have = 0
#         need = len(t)
#         for c in t:
#             tCount[c] = 1 + tCount.get(c, 0)
        
#         for r in range(len(s)):
#             c = s[r]
#             window[c] = 1 + window.get(c, 0)
            
#             if c in window:
#                 have += 1
            
#             while have == need:
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            if c in countT and window[c] == countT[c]:
                have += 1
        
            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1]
                
            
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flips = 0
        num1 = 0
        
        for c in s:
            if c == '1':
                num1 += 1
            else:
                if num1 > 0:
                    flips += 1
                    num1 -= 1
        return flips
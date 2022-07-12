class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flips = 0
        potential = 0
        for c in s:
            if c == '1':
                potential += 1
            elif potential > 0:
                flips += 1
                potential -= 1
        
        return flips
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flip = 0
        num1 = 0
        for c in s:
            if c == '1':
                num1 += 1
            else:
                if num1 > 0:
                    flip += 1
                    num1 -= 1
        return flip
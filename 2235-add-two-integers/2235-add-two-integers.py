class Solution:
    def sum(self, num1: int, num2: int) -> int:

        mask = 0xffffffff
        while num2 != 0:
            tmp = (num1 & num2) << 1
            num1 = (num1 ^ num2) & mask
            num2 = tmp & mask
        if num1 > mask // 2:
            return ~(num1 ^ mask)
        else:
            return num1


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            if digits[i] > 9:
                digits[i] %= 10
            else:
                carry = 0
        
        if carry > 0:
            return [1] + digits
        return digits
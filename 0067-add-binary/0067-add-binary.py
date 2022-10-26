class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aP = len(a) - 1
        bP = len(b) - 1
        carry = 0
        res = ''
        
        while aP >= 0 or bP >= 0 or carry:
            if aP >= 0:
                carry += int(a[aP])
                aP -= 1
            if bP >= 0:
                carry += int(b[bP])
                bP -= 1
            
            res += str((carry % 2))
            carry //= 2
        return res[::-1]
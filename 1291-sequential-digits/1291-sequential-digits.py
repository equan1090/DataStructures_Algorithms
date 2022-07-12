class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = '123456789'
        res = []
        lowLen = len(str(low))
        hiLen = len(str(high))
        
        for i in range(lowLen, hiLen + 1):
            for j in range(10-i):
                num = int(digits[j: j+i])
                if num >= low and num <= high:
                    res.append(num)
        return res
                
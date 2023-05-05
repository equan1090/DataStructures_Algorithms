class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        res = [''] * numRows
        i = 0
        step = 1
        
        for c in s:
            res[i] += c
            
            if i == 0:
                step = 1
            elif i == numRows - 1:
                step = -1
            
            i += step
        return ''.join(res)
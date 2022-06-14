class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        p = [0] * 50000 # 1D number array
        ans = []
        for (start,end) in paint:
            res = 0
            # loop from start to end of the interval
            while start < end : 
                # if jump value is set
                if p[start] != 0 : 
                    start = p[start]
                # if jump value is not set
                else :
                    res += 1
                    p[start] = end
                    start += 1
            ans.append(res)
        return ans
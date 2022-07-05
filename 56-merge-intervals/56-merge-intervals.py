class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals, key=lambda x: x[0])
        
        for val in intervals:
            if not res or val[0] > res[-1][-1]:
                res.append(val)
            else:
                res[-1] = [res[-1][0], max(res[-1][-1], val[-1])]
                
        return res
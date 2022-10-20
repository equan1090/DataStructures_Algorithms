class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        for val in (intervals):
            if not res or res[-1][-1] < val[0]:
                res.append(val)
            else:
                res[-1] = [res[-1][0], max(res[-1][-1], val[1])]
        return res
                
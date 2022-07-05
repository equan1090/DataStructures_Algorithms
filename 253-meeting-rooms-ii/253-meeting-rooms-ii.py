class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([i[-1] for i in intervals])
        
        res = 0
        count = 0
        i = j = 0
        while i < len(intervals):
            if start[i] < end[j]:
                i += 1
                count += 1
            else:
                j += 1
                count -= 1
            res = max(res, count)
        return res
        
        
        
        
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        res = float('-inf')
        start = sorted([x[0] for x in intervals])
        end = sorted([x[1] for x in intervals])
        count = 0
        
        i = j = 0
        while i < len(intervals):
            if start[i] < end[j]:
                count += 1
                i += 1
            else:
                j += 1
                count -= 1
            
            res = max(count, res)
        return res
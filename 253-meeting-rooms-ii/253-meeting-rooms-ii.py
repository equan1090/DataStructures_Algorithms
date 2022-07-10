class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        '''
        start = [0,   5, 15]
        end   = [10, 20, 30]
        0 ------------------------ 30
            5-----10
                       15----20 
        '''
        
        start = sorted([x[0] for x in intervals])
        end = sorted([x[1] for x in intervals])
        
        count = 0
        res = 0
        i = j = 0
        while i < len(start):
            if start[i] < end[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            res = max(count, res)
        return res
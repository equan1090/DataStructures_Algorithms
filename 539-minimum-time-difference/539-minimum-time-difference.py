class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        for i, t in enumerate(timePoints):
            hours, minutes = t.split(':')
            totalTime = (int(hours)*60) + int(minutes)
            
            timePoints[i] = totalTime
        
        timePoints.sort()
        
        res = 1440 + timePoints[0] - timePoints[-1]
        
        for i in range(1, len(timePoints)):
            res = min(res, timePoints[i] - timePoints[i - 1])
        return res
        
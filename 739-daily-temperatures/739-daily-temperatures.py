class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        
        for idx, temps in enumerate(temperatures):
            while stack and stack[-1][-1] < temps:
                i, t = stack.pop()
                res[i] = idx - i
                
            stack.append([idx, temps])
        return res
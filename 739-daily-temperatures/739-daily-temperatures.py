class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, tmp in enumerate(temperatures):
            while stack and tmp > stack[-1][-1]:
                idx, prevTmp = stack.pop()
                res[idx] = i - idx
                
            stack.append((i, tmp))
        return res
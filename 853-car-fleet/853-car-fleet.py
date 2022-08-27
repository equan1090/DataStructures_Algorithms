class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = [[p, s] for p, s in zip(position, speed)]
        
        pairs.sort(reverse=True)
        
        for p, s in pairs:
            stack.append((target - p) / s)
            while len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
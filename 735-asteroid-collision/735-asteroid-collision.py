class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for rock in asteroids:
            while stack and rock < 0 and stack[-1] > 0:
                diff = rock + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    rock = 0
                else:
                    rock = 0
                    stack.pop()
            if rock:   
                stack.append(rock)
        return stack
        
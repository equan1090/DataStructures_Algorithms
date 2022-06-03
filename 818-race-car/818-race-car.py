class Solution:
    def racecar(self, target: int) -> int:
        q = deque([(0, 0, 1)])
        visited = set((0, 0, 1))
        while q:
            pos, move, speed = q.popleft()
            if pos == target:
                return move
            
            
            if (pos, speed) not in visited:
                visited.add((pos, speed))
                q.append((pos + speed, move + 1, speed * 2))
            
                if (pos + speed > target and speed > 0) or (pos + speed < target and speed < 0):
                    q.append((pos, move + 1, -1 if speed > 0 else 1))
                    
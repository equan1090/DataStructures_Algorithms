class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = deque([])
        visited = set()
        
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
                    
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nR = r + dr
                nC = c + dc
                rowbounds = 0 <= nR < len(rooms)
                colbounds = 0 <= nC < len(rooms[0])
                
                if rowbounds and colbounds and (nR, nC) not in visited and rooms[nR][nC] != -1:
                    rooms[nR][nC] = rooms[r][c] + 1
                    visited.add((nR, nC))
                    q.append((nR, nC,))
        return rooms
            
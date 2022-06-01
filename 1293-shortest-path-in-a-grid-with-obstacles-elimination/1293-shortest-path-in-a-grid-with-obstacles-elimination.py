class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = deque([(0, 0, 0, k)])
        visited = set((0, 0, 0))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        while q:
            r, c, distance, demo = q.popleft()
            
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return distance
            
            for dr, dc in directions:
                nRow = dr + r
                nCol = dc + c
                rowbounds = 0 <= nRow < len(grid)
                colbounds = 0 <= nCol < len(grid[0])
                pos = (nRow, nCol, demo)
                
                if rowbounds and colbounds and pos not in visited:
                    visited.add(pos)
                    if grid[nRow][nCol] == 1 and demo > 0:
                        q.append((nRow, nCol, distance + 1, demo - 1))
                    if grid[nRow][nCol] == 0:
                        q.append((nRow, nCol, distance + 1, demo))
        return -1
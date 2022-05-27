class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        visited = set()
        q = deque([(0, 0, 0, k)])
        
        while q:
            r, c, distance, demo = q.popleft()
            
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return distance
            
            deltas = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            for x, y in deltas:
                nRow = r + x
                nCol = c + y
                rowBounds = 0 <= nRow < len(grid)
                colBounds = 0 <= nCol < len(grid[0])
                pos = (nRow, nCol, demo)
                if rowBounds and colBounds and pos not in visited:
                    if grid[nRow][nCol] == 1 and demo > 0:
                        visited.add(pos)
                        q.append((nRow, nCol, distance + 1, demo - 1))
                    elif grid[nRow][nCol] == 0:
                        visited.add(pos)
                        q.append((nRow, nCol, distance + 1, demo))
        return -1
            
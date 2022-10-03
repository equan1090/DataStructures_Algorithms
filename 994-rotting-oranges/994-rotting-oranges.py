class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        res = 0
        fresh = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q and fresh > 0:
            
            for i in range(len(q)):
                r, c = q.popleft()
                
                
                for dr, dc in directions:
                    nRow = r + dr
                    nCol = c + dc
                    
                    rowbounds = 0 <= nRow < len(grid)
                    colbounds = 0 <= nCol < len(grid[0])
                    
                    if rowbounds and colbounds and grid[nRow][nCol] == 1:
                        q.append((nRow, nCol))
                        grid[nRow][nCol] = 2
                        fresh -= 1
            res += 1
        return res if fresh == 0 else -1
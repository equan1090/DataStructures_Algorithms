class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        grid = [
        [2,1,1],
        [0,1,1],
        [1,0,1]]
        '''
        q = deque([])
        good = 0
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    good += 1
        
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q and good > 0:
            
            for i in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nRow = dr + r
                    nCol = dc + c
                    rowbounds = 0 <= nRow < len(grid)
                    colbounds = 0 <= nCol < len(grid[0])
                    if rowbounds and colbounds and grid[nRow][nCol] == 1:
                        grid[nRow][nCol] = 2
                        q.append((nRow, nCol))
                        good -= 1
                    else:
                        continue
            res += 1
        
        return res if good == 0 else -1
        
        
        
        
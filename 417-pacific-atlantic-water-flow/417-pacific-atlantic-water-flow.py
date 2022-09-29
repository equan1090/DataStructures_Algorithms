class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        ROWS = len(heights)
        COLS = len(heights[0])
        for r in range(ROWS):
            self.dfs(heights, r, 0, pacific, heights[r][0])
            self.dfs(heights, r, COLS - 1, atlantic, heights[r][COLS - 1])
            
        for c in range(COLS):
            self.dfs(heights, 0, c, pacific, heights[0][c])
            self.dfs(heights, ROWS - 1, c, atlantic, heights[ROWS-1][c])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
                    
        return res
    
    def dfs(self, heights, r, c, visited, prev):
        rowbounds = 0 <= r < len(heights)
        colbounds = 0 <= c < len(heights[0])
        
        if not rowbounds or not colbounds or (r, c) in visited or heights[r][c] < prev:
            return
        
        visited.add((r, c))
        
        self.dfs(heights, r + 1, c, visited, heights[r][c])
        self.dfs(heights, r - 1, c, visited, heights[r][c])
        self.dfs(heights, r, c + 1, visited, heights[r][c])
        self.dfs(heights, r, c - 1, visited, heights[r][c])
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                potential = self.findIsland(grid, r, c, visited)
                res = max(res, potential)
        return res
    
    def findIsland(self, grid, r, c, visited):
        rowbounds = 0 <= r < len(grid)
        colbounds = 0 <= c < len(grid[0])
        if not rowbounds or not colbounds or (r, c) in visited or grid[r][c] == 0:
            return 0
        
        visited.add((r, c))
        
        size = 1
        
        size += self.findIsland(grid, r + 1, c, visited)
        size += self.findIsland(grid, r - 1, c, visited)
        size += self.findIsland(grid, r, c + 1, visited)
        size += self.findIsland(grid, r, c - 1, visited)
        return size
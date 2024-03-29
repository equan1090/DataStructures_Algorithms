class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.findIsland(grid, r, c, visited):
                    count += 1
        return count
    
    def findIsland(self, grid, r, c, visited):
        rowbounds = 0 <= r < len(grid)
        colbounds = 0 <= c < len(grid[0])
        
        if not rowbounds or not colbounds or grid[r][c] == '0' or (r, c) in visited:
            return False
        
        visited.add((r, c))
        
        self.findIsland(grid, r + 1, c, visited)
        self.findIsland(grid, r - 1, c, visited)
        self.findIsland(grid, r, c + 1, visited)
        self.findIsland(grid, r, c - 1, visited)
        
        return True
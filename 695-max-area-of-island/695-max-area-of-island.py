class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                attempt = self.traverse(grid, r, c, visited)
                res = max(res, attempt)
        return res
    
    
    def traverse(self, grid, r, c, visited):
        rowbounds = 0 <= r < len(grid)
        colbounds = 0 <= c < len(grid[0])
        
        if not rowbounds or not colbounds:
            return 0
        
        if grid[r][c] == 0:
            return 0
        
        pos = (r, c)
        if pos in visited:
            return 0
        visited.add(pos)
        
        size = 1
        size += self.traverse(grid, r + 1, c, visited)
        size += self.traverse(grid, r - 1, c, visited)
        size += self.traverse(grid, r, c + 1, visited)
        size += self.traverse(grid, r, c - 1, visited)
        return size
    
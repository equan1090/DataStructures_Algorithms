class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.traverse(grid, r, c, visited):
                    count += 1
        return count
        
        
    def traverse(self, grid, r, c, visited):
        rowbounds = 0 <= r < len(grid)
        colbounds = 0 <= c < len(grid[0])
        
        if not rowbounds or not colbounds or grid[r][c] == '0':
            return False
        
        if (r, c) in visited:
            return False
        
        visited.add((r, c))
        
        self.traverse(grid, r + 1, c, visited)
        self.traverse(grid, r - 1, c, visited)
        self.traverse(grid, r, c + 1, visited)
        self.traverse(grid, r, c - 1, visited)
        
        return True
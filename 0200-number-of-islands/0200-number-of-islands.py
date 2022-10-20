class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.dfs(grid, r, c, visited):
                    count += 1
        return count
    
    def dfs(self,grid, r, c, visited):
        rowbounds = 0 <= r < len(grid)
        colbounds = 0 <= c < len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        if not rowbounds or not colbounds or (r, c) in visited or grid[r][c] == '0':
            return False
        
        visited.add((r, c))
        
        self.dfs(grid, r + 1, c, visited)
        self.dfs(grid, r - 1, c, visited)
        self.dfs(grid, r, c + 1, visited)
        self.dfs(grid, r, c - 1, visited)
        return True
        
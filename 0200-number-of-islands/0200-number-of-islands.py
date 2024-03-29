class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.dfs(grid, r, c, visited):
                    count += 1
        return count
    def dfs(self, grid, r, c, visited):
        rowbounds = 0 <= r < len(grid)
        colbounds = 0 <= c < len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        if not rowbounds or not colbounds or grid[r][c] == '0' or (r, c) in visited:
            return False
        
        visited.add((r, c))
        
        for dr, dc in directions:
            self.dfs(grid, r + dr, c + dc, visited)

        return True
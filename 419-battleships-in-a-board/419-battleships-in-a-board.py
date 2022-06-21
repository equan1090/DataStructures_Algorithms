class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        visited = set()
        count = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.dfs(board, r, c, visited):
                    count += 1
        return count
    
    def dfs(self, board, r, c, visited):
        pos = (r, c)
        
        rowbounds = 0 <= r < len(board)
        colbounds = 0 <= c < len(board[0])
        
        if not rowbounds or not colbounds or board[r][c] == '.' or pos in visited:
            return False
        
        visited.add(pos)
        
        self.dfs(board, r + 1, c, visited)
        self.dfs(board, r - 1, c, visited)
        self.dfs(board, r, c + 1, visited)
        self.dfs(board, r, c - 1, visited)
        
        return True
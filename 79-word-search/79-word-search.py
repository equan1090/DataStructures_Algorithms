class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.dfs(board, r, c, word, 0, visited):
                    return True
        return False
    
    def dfs(self, board, r, c, word, i, visited):
        rowbounds = 0 <= r < len(board)
        colbounds = 0 <= c < len(board[0])
        
        if i == len(word):
            return True
        
        if not rowbounds or not colbounds or word[i] != board[r][c] or (r, c) in visited:
            return False
        
        visited.add((r, c))
        
        res = (
                self.dfs(board, r + 1, c, word, i+1, visited) or
            self.dfs(board, r - 1, c, word, i+1, visited) or
            self.dfs(board, r, c + 1, word, i+1, visited) or
            self.dfs(board, r, c - 1, word, i+1, visited)
        
        )

        
        visited.remove((r, c))
        return res
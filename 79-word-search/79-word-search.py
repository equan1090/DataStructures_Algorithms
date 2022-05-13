class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.traverse(board, r, c, 0, word, visited):
                    return True
        return False
        
    def traverse(self, board, r, c, i, word, visited):
        rowbounds = 0 <= r < len(board)
        colbounds = 0 <= c < len(board[0])
        
        if i == len(word):
            return True
        
        if not rowbounds or not colbounds:
            return False
        
        if word[i] != board[r][c]:
            return False
        
        pos = (r, c)
        if pos in visited:
            return False
        visited.add(pos)
        
        res = (
            self.traverse(board, r + 1, c, i + 1, word, visited) or
            self.traverse(board, r - 1, c, i + 1, word, visited) or
            self.traverse(board, r, c + 1, i + 1, word, visited) or
            self.traverse(board, r, c - 1, i + 1, word, visited)
        )
        visited.remove(pos)
        return res
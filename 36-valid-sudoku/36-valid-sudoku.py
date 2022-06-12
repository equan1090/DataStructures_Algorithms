class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                pos = board[r][c]
                if pos == '.':
                    continue
                
                if pos in rows[r] or pos in cols[c] or pos in square[(r//3, c//3)]:
                    return False
                
                rows[r].add(pos)
                cols[c].add(pos)
                square[(r//3, c//3)].add(pos)
        return True
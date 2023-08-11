class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = defaultdict(set)
        COLS = defaultdict(set)
        SQR = defaultdict(set)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                pos = board[r][c]
                if pos == '.':
                    continue
                
                if pos in ROWS[r] or pos in COLS[c] or pos in SQR[(r // 3, c // 3)]:
                    return False
                
                ROWS[r].add(pos)
                COLS[c].add(pos)
                SQR[(r // 3, c // 3)].add(pos)
        return True
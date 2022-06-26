class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                pos = board[r][c]
                if pos == '.':
                    continue
                
                if pos in rows[r] or pos in cols[c] or pos in squares[(r // 3, c // 3)]:
                    return False
                
                rows[r].append(pos)
                cols[c].append(pos)
                squares[(r//3,c//3)].append(pos)
        return True
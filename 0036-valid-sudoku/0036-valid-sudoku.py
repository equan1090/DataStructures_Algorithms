class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                pos = board[r][c]
                if pos == '.':
                    continue
                
                if pos in row[r] or pos in col[c] or pos in square[(r // 3, c // 3)]:
                    return False
            
                row[r].add(pos)
                col[c].add(pos)
                square[(r//3, c//3)].add(pos)
        return True
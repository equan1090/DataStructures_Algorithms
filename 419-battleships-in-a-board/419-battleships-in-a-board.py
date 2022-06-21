class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0
        
        output =0
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]=='.':
                    continue
                if r > 0 and board[r-1][c] == 'X':
                    continue
                if c > 0 and board[r][c-1] == 'X':
                    continue
                output +=1
        return output
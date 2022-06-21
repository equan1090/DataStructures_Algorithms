class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0
        
        output =0
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='.':
                    continue
                if i > 0 and board[i-1][j] == 'X':
                    continue
                if j > 0 and board[i][j-1] == 'X':
                    continue
                output +=1
        return output
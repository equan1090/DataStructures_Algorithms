class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        return self.dfs(n, n, '', [])
        
    def dfs(self, opened, closed, path, res):
        
        if opened > closed or opened < 0 or closed < 0:
            return
        
        if opened == 0 and closed == 0:
            res.append(''.join(path))
            return
        
        self.dfs(opened - 1, closed, path + '(', res)
        self.dfs(opened, closed - 1, path + ')', res)
        
        return res
        
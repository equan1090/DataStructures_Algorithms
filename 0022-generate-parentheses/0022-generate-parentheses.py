class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.dfs(n, n, '', [])
    def dfs(self, opened, closed, path, res):
        if closed < opened or closed < 0 or opened < 0:
            return
        
        if opened == 0 and closed == 0:
            res.append(path)
        
        self.dfs(opened - 1, closed, path + '(', res)
        self.dfs(opened, closed - 1, path + ')', res)
        
        return res
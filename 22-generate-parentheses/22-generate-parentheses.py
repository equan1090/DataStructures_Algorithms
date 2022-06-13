class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(n, n, [], res)
        return res
    
    def dfs(self, opened, closed, path, res):
        # if we ever have more opened than closes remaining, then that means we added a closed before an open parentheses
        # example we start with 3 opened, 3 closed, if we end up inputting '())', that means we have 2 opened left with 1 closed left, 3 - 1 vs 3 - 2
        if opened > closed or opened < 0 or closed < 0:
            return
        
        if opened == 0 and closed == 0:
            res.append(''.join(path))
        
        self.dfs(opened - 1, closed, path + ['('], res)
        self.dfs(opened, closed - 1, path + [')'], res)
        return res
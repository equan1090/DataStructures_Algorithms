from collections import deque
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        
        self.permute(s, [], 0, res)
        return res
        
    def permute(self, s, path, i, res):
        if len(path) == len(s):
            res.append(''.join(path))
            return
        
        self.permute(s, path + [s[i]], i + 1, res)
        
        if s[i].isalpha():
            self.permute(s, path + [s[i].swapcase()], i + 1, res)
        
        
        
            
            
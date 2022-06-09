class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        self.permute(s, [], 0, res)
        return res
        
    def permute(self, s, path, i, res):
        if len(path) == len(s):
            res.append(''.join(path))
            return
        
        if s[i].isalpha():
            path.append(s[i].lower())
            self.permute(s, path, i+1, res)
            path.pop()
            path.append(s[i].upper())
            self.permute(s, path, i+1, res)
            path.pop()
        else:
            path.append(s[i])
            self.permute(s, path, i+1, res)
            path.pop()
            
        
        
            
            
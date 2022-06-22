class Solution:
    def lengthLongestPath(self, input: str) -> int:
        paths = {}
        res = 0
        chunks = input.split('\n')
        
        for c in chunks:
            level = 0
            
            while level < len(c) and c[level] == '\t':
                level += 1
            
            length = len(c) if level == 0 else paths[level - 1] + 1 + len(c[level:])
            
            if '.' in c:
                res = max(res, length)
            else:
                paths[level] = length
        return res
        
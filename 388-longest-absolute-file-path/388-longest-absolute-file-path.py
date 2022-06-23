class Solution:
    def lengthLongestPath(self, input: str) -> int:
        '''
        "dir
        \tsubdir1
        \t\tfile1.ext
        \t\tsubsubdir1
        \tsubdir2
        \t\tsubsubdir2
        \t\t\tfile2.ext"
        '''
        dic = {}
        res = 0
        chunks = input.split('\n')
        
        for c in chunks:
            level = 0
            
            while c[level] == '\t':
                level += 1
            
            curLen = len(c) if level == 0 else dic[level - 1] + 1 + len(c[level:])
            
            if '.' in c:
                res = max(res, curLen)
            else:
                dic[level] = curLen
        return res
            
        
        
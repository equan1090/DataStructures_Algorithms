class Solution:
    def lengthLongestPath(self, s: str) -> int:
        paths = s.split('\n')
        stack = []
        res = 0

        for path in paths:
            p = path.split('\t')
            depth = len(p) - 1
            name = p[-1]
            l = len(name)
            while stack and stack[-1][1] >= depth: 
                stack.pop()
            if not stack: 
                stack.append((l, depth))
            else: 
                stack.append((l+stack[-1][0], depth))
            if '.' in name: 
                res = max(res, stack[-1][0] + stack[-1][1])   
        return res
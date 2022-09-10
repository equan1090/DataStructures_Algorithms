class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        res = ''
        for i in s:
            if not stack:
                stack.append([i,1])
                continue
            if stack[-1][0] == i:
                stack[-1][1] += 1
            else:
                stack.append([i,1])
            if stack[-1][1] == k:
                stack.pop()
        
        for char, num in stack:
            res += char*num
        return res
            
            
            
        '''
        [d, 1] [e, 3] d
        '''
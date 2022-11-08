class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        res = []
        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append([c, 1])
            
            else:
                stack[-1][-1] += 1   
                
            if stack and stack[-1][-1] == k:
                stack.pop()
        
        for char, num in stack:
            res.append(char * num)
        return ''.join(res)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def helper(string):
            stack = []
            for val in string:
                if val == '#':
                    if not stack:
                        continue
                    stack.pop()
                else:
                    stack.append(val)
            return stack
        
        return helper(s) == helper(t)
            
                    
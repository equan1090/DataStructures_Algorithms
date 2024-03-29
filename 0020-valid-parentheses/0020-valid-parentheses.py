class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        
        stack = []
        for c in s:
            if c in pairs.values():
                stack.append(c)
            
            else:
                if not stack or pairs[c] != stack.pop():
                    return False
        return len(stack) == 0
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        
        for c in s:
            if c in pairs.values():
                stack.append(c)
            else:
                if not stack or pairs[c] != stack.pop():
                    return False
        return len(stack) == 0
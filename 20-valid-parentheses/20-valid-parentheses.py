class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for val in s:
            if val in pairs.values():
                stack.append(val)
            else:
                if not stack or pairs[val] != stack.pop():
                    return False
        return len(stack) == 0
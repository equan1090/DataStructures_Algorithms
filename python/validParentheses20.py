'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
'''
def isValid(s):
    pairs = {
        '}': '{',
        ')': '(',
        ']': '[',
    }
    stack = []
    for char in s:
        if char in pairs.values():
            stack.append(char)
        else:
            if not stack or pairs[char] != stack.pop():
                return False
    return len(stack == 0)

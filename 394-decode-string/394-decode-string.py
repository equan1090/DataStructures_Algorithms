class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        curStr = ''
        for c in s:
            if c.isdigit():
                num = (10 * num) + int(c)
            elif c == '[':
                stack.append((num, curStr))
                num = 0
                curStr = ''
            elif c == ']':
                prevNum, prevStr = stack.pop()
                curStr = prevStr + (curStr * prevNum)
            else:
                curStr += c
        return curStr
            
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for c in tokens:
            if c not in '/*-+':
                stack.append(int(c))
            else:
                right, left = stack.pop(), stack.pop()
                if c == '+':
                    stack.append(left + right)
                elif c == '-':
                    stack.append(left - right)
                elif c == '*':
                    stack.append(left * right)
                else:
                    stack.append(int(left / right))
        return stack.pop()
                
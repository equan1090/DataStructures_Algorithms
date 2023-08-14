class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for val in tokens:
            if val not in '/*-+':
                stack.append(int(val))
            else:
                right = stack.pop()
                left = stack.pop()
                if val == '+':
                    stack.append(left + right)
                elif val == '-':
                    stack.append(left - right)
                elif val == '*':
                    stack.append(left * right)
                else:
                    stack.append(int(left / right))
        return stack.pop()
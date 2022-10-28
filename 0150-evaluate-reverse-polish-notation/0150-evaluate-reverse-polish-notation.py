class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for val in tokens:
            if val not in '+-*/':
                stack.append(int(val))
            else:
                right, left = stack.pop(), stack.pop()
                if val == '+':
                    stack.append(right + left)
                elif val == '-':
                    stack.append(left - right)
                elif val == '*':
                    stack.append(left * right)
                else:
                    stack.append(int(left / right))
        return stack.pop()
    '''
    
    [10 6 -132 ]
    
    '''
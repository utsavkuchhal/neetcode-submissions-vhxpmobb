class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['/', '+', '-', '*']:
                right = int(stack.pop())
                left = int(stack.pop())
                if token == '+':
                    temp = right + left
                elif token == '/':
                    temp = int(left / right)
                elif token == '-':
                    temp = left - right
                elif token == '*':
                    temp = left * right
                stack.append(temp)
            else:
                stack.append(token)
        return int(stack[0])
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ['[', '(', '{']:
                stack.append(char)
                continue
            if char in [')', ']', '}'] and not stack:
                return False
            if char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == ')' and stack[-1] == '(':
                stack.pop()
            else:
                return False
        
        return True if not stack else False
        
            
class MinStack:

    def __init__(self):
        self.stack = list()
        self.min_stack = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        top = self.stack.pop()
        if self.min_stack and top == self.min_stack[-1]:
            self.min_stack.pop()
        return top

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        

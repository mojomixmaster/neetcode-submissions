class MinStack:

    def __init__(self):
        self.stack = [] # initialise the stack attribute of the object to an empty list
        self.minvaluestack = []

    def push(self, val: int) -> None:
        stack = self.stack
        stack.append(val)
        self.minvaluestack.append(min(val, self.minvaluestack[-1]) if self.minvaluestack else val)

    def pop(self) -> None:
        stack = self.stack
        stack.pop()
        self.minvaluestack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minvaluestack[-1]

class MinStack:

    def __init__(self):
        self.stack = [None] # initialise the stack attribute of the object to an empty list
        self.minvaluestack = [None]

    def push(self, val: int) -> None:
        print(f"pushing {val}, min value is {min(val, self.minvaluestack[-1] if self.minvaluestack[-1] else val)}")
        stack = self.stack
        stack.append(val)
        self.minvaluestack.append(min(val, self.minvaluestack[-1]) if self.minvaluestack[-1] is not None else val)

    def pop(self) -> None:
        stack = self.stack
        stack.pop()
        self.minvaluestack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minvaluestack[-1]

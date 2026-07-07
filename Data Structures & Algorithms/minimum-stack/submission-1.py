class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack and self.minStack[-1] >= val:
            self.minStack.append(val)
        else:
            self.minStack.appendleft(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minStack[-1]:
            self.minStack.pop()
        else:
            self.minStack.popleft()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]

class MinStack:

    def __init__(self):
        self._stack = []
        self._minStack = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if self._minStack:
            val = min(self._minStack[-1], val)
        self._minStack.append(val)
        
    def pop(self) -> None:
        self._stack.pop()
        self._minStack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
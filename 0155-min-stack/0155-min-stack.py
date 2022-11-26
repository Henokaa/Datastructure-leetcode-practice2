class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if self.stack:
            small = min(self.stack[-1][1], val)
            self.stack.append((val,small))
            
        else:
            self.stack.append((val, val))
        

    def pop(self) -> None:
        val, small  = self.stack.pop()
        return val
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
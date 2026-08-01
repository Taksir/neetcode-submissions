class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if (self.minstack and self.minstack[-1] >= val) or not self.minstack:
            self.minstack.append(val)
    def pop(self) -> None:        
        if self.stack.pop() == self.minstack[-1]:
            self.minstack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minstack[-1]

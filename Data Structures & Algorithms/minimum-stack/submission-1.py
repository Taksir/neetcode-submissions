class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        if self.stack:
            self.mins.append(min(val, self.mins[-1]))
        else:
            self.mins.append(val)
        self.stack.append(val)
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]

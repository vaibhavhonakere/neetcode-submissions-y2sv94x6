class MinStack:

    def __init__(self):
        self.minStack = []
        self.normal = []

    def push(self, val: int) -> None:
        self.normal.append(val)
        if(self.minStack):
            self.minStack.append(min(self.minStack[-1], val))
        else:
            self.minStack.append(val)
        
    def pop(self) -> None:
        self.minStack.pop()
        self.normal.pop()

    def top(self) -> int:
        return self.normal[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        

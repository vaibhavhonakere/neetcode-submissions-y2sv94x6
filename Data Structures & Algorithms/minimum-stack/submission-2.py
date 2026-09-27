class MinStack:

    def __init__(self):
        # two stacks
        self.min_stack = []
        self.normal_stack = []

    def push(self, val: int) -> None:
        self.normal_stack.append(val)
        if(not(self.min_stack)):
            self.min_stack = [val]
        else:
            self.min_stack.append(min(self.min_stack[-1], val))

    def pop(self) -> None:
        self.min_stack.pop()
        self.normal_stack.pop()

    def top(self) -> int:
        return self.normal_stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]

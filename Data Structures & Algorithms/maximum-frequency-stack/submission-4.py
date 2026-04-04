class FreqStack:

    def __init__(self):
        self.countMap = {}
        self.freqStack = defaultdict(list)
        self.maxFreq = 1

    def push(self, val: int) -> None:
        if(val in self.countMap):
            self.countMap[val] += 1
        else:
            self.countMap[val] = 1
        self.maxFreq = max(self.maxFreq, self.countMap[val])
        self.freqStack[self.countMap[val]].append(val)
        
    def pop(self) -> int:
        tmp = self.freqStack[self.maxFreq].pop()
        self.countMap[tmp] -= 1
        if(not(self.freqStack[self.maxFreq])):
            del self.freqStack[self.maxFreq]
            self.maxFreq -= 1
        return tmp

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
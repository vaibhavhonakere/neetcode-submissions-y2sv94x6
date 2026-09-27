class FreqStack:
    ### Have a hashmap of a key value pair from
    ### num_freq : [nums...](e.x [1,2,3]).  if the input at the time is s = "[1,2,3]"
    ###
    ### next input is s = "[1,2,3,1,2]"
    ### num_freq : [1,2])
    ### ... same for all them and then when we pop, we would pop the last key, 
    ## and pop the last element. 

    def __init__(self):
        self.max_stack = {}
        self.num_freq = {}
        self.max_count = 1

    def push(self, val: int) -> None:
        self.num_freq[val] = self.num_freq.get(val, 0) + 1
        
        self.max_count = max(self.max_count, self.num_freq[val])
        if(self.max_count not in self.max_stack):
            self.max_stack[self.num_freq[val]] = [val]
        else:
            self.max_stack[self.num_freq[val]].append(val)

    def pop(self) -> int:
        # print (self.max_stack)
        tmp = self.max_stack[self.max_count].pop()
        self.num_freq[tmp] -= 1
        if(len(self.max_stack[self.max_count]) == 0):
            del self.max_stack[self.max_count]
            self.max_count -= 1
        return tmp
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
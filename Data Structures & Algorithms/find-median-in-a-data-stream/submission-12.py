class MedianFinder:

    def __init__(self):
        self.max_heap = [] # should be the first half numbers(e.g [0,1,2,3]) 
        self.min_heap = [] # should be the second half numbers(e.g [4,5,6,7])
        # We will make the rule that max_heap will always be bigger
        # by at most one element
        
    def addNum(self, num: int) -> None:
        # heapq.heappush(self.min_heap,num)
        if(self.min_heap and self.min_heap[0] < num):
            # val = heapq.heappop_max(self.max_heap)
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush_max(self.max_heap, num)
        
        if(len(self.min_heap) + 1 < len(self.max_heap)):
            max_val = heapq.heappop_max(self.max_heap)
            heapq.heappush(self.min_heap, max_val)
        elif(len(self.min_heap) > len(self.max_heap) + 1):
            min_val = heapq.heappop(self.min_heap)
            heapq.heappush_max(self.max_heap, min_val)
        
        

    def findMedian(self) -> float:
        # print(self.max_heap, self.min_heap)
        if(len(self.max_heap) == len(self.min_heap)):
            return (float)((self.max_heap[0] + self.min_heap[0]) / (2.0))
        elif(len(self.max_heap) > len(self.min_heap)):
            return self.max_heap[0]
        else:
            return self.min_heap[0]
        
        
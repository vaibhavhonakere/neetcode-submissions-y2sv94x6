class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k
        for n in nums:
            heapq.heappush(self.minHeap, n)
            if(len(self.minHeap) > k):
                heapq.heappop(self.minHeap)
        print("first, ", self.minHeap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if(len(self.minHeap) > self.k):
            heapq.heappop(self.minHeap)
        print(self.minHeap, val)
        return self.minHeap[0]

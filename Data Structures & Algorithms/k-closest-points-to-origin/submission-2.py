class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i, (x1,y1) in enumerate(points):
            dist = (((x1)**2 + (y1)**2)**0.5)
            heapq.heappush(minHeap, (-dist, (x1, y1)))
            if(len(minHeap) > k):
                heapq.heappop(minHeap)
        
        res = []
        while(minHeap):
           _, point = heapq.heappop(minHeap)
           res.append([point[0], point[1]])
        return res
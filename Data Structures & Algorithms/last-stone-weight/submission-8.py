class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_max_heap = []
        for s in stones:
            heapq.heappush_max(stones_max_heap, s)
        
        while(len(stones_max_heap) > 1):
            first = heapq.heappop_max(stones_max_heap)
            second = heapq.heappop_max(stones_max_heap)

            if(second < first):
                heapq.heappush_max(stones_max_heap, first - second)
        
        return stones_max_heap[0] if stones_max_heap else 0


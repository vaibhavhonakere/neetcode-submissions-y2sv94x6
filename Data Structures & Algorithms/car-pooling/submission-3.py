class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])

        # have a min_queue
        min_heap = [] # (dest, num_pass)
        
        cap = 0
        for (num_pass, source, dest) in trips:
            while(min_heap and min_heap[0][0] <= source):
                _, passenger = heapq.heappop(min_heap)
                cap -= passenger
            
            if(cap + num_pass <= capacity):
                heapq.heappush(min_heap, (dest, num_pass))
                cap += num_pass
            else:
                return False
        
        return True
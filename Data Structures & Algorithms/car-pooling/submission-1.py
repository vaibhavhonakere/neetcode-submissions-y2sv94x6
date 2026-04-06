class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # [[1,1,4],[5,2,3], [3,2,4]]
        # sort the trips
        trips.sort(key=lambda x: x[1])

        # have a min_queue
        min_heap = [] # (dest, num_pass)

        cap = 0
        for (num_pass, source, dest) in trips:

            while(min_heap and min_heap[0][0] <= source):
                dst, passengers = heapq.heappop(min_heap)
                cap -= passengers
        
            if(cap + num_pass <= capacity):
                heapq.heappush(min_heap, (dest, num_pass))
                cap += num_pass
            else:
                return False
            
        
        return True



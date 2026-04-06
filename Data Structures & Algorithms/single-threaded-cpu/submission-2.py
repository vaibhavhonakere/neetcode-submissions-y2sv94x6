class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # use the heapq and store 
        # (enque_time, processing_time, index)

        # Queue add the tasks that can't be processed
        # at that exact time

        # (1, 4, 0), (2, 1, 2), (3, 3, 1)
        # (2,1,3), (3,3,4), (4, 1, 2), (4, 4, 1), (5, 2, 0)

        pending = [] # (enque_time, processing_time, index)
        available = [] # (processing_time, index)

        for i, (enque_time, processing_time) in enumerate(tasks):
            heapq.heappush(pending, (enque_time, processing_time, i))
        
        time = 0
        ret = []

        while(pending or available):
            while(pending and pending[0][0] <= time):
                _, processing_time, index = heapq.heappop(pending)
                heapq.heappush(available, (processing_time, index))

            if(not(available)):
                time = pending[0][0]
                continue
            
            proc_time, i = heapq.heappop(available)
            time += proc_time
            ret.append(i)

        return ret

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        max_heap = []

        for key, value in count.items():
            heapq.heappush_max(max_heap, (value, key))
        
        queue = deque([])
        cycles = 0
        while(max_heap or queue):
            if(max_heap):
                num, char = heapq.heappop_max(max_heap)
                num -= 1
                if(num > 0):
                    queue.append((cycles + n, num, char))
            else:
                if(queue):
                    cycles = queue[0][0]
            
            if(queue and cycles == queue[0][0]):
                _, num_chars, char = queue.popleft()
                heapq.heappush_max(max_heap, (num_chars, char))

            cycles += 1
        
        return cycles

        # for key, freq in count.items():
        #     heapq.heappush_max(max_heap, (freq, key))

        # time = 0
        # queue = deque([]) # (time, key, cnt)

        # while(max_heap or queue):
        #     time += 1
        #     if(max_heap):
        #         num, ch = heapq.heappop_max(max_heap)
        #         num -= 1
        #         if(num > 0):
        #             queue.append((time + n, ch, num))
        #     else:
        #         time = queue[0][0]
            
        #     if(queue and time == queue[0][0]):
        #         _, old_char, old_cnt = queue.popleft()
        #         heapq.heappush_max(max_heap, (old_cnt, old_char))
        
        # return time
            
            




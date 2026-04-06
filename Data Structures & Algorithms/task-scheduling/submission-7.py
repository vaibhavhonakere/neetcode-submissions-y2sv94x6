class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        max_heap = []

        for key, freq in count.items():
            heapq.heappush_max(max_heap, (freq, key))

        time = 0
        queue = deque([]) # (time, key, cnt)

        while(max_heap or queue):
            time += 1
            # print(queue)
            # print(max_heap, time)
            if(max_heap):
                num, ch = heapq.heappop_max(max_heap)
                num -= 1
                if(num > 0):
                    queue.append((time + n, ch, num))
            
            if(queue and time == queue[0][0]):
                _, old_char, old_cnt = queue.popleft()
                heapq.heappush_max(max_heap, (old_cnt, old_char))
        
        return time
            
            




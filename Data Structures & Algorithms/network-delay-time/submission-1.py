class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj_map = defaultdict(list)
        for u,v,t in times:
            adj_map[u].append([v,t])
        
        min_heap = [(0, k)]
        visit = set()
        time = 0

        while(min_heap):
            time, signal = heapq.heappop(min_heap)
            if(signal in visit):
                continue 
            visit.add(signal)
            if(len(visit) == n):
                return time
            for nei, t_2 in adj_map[signal]:
                heapq.heappush(min_heap,(time + t_2, nei))
        
        return -1
            




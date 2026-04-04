class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjMap = defaultdict(list)

        for u,v, weight in flights:
            adjMap[u].append([v, weight])
        
        def dijkstra(node):
            queue = [(0, 0, node)]
            visited = set()
            while(queue):
                price, cnt, n = heapq.heappop(queue)
                if(cnt > k + 1):
                    continue
                if(n == dst):
                    return price
                visited.add(n)
                for nei, cost in adjMap[n]:
                    if(nei in visited):
                        continue
                    heapq.heappush(queue, (price + cost, cnt + 1, nei))
            
            return -1
            
        return dijkstra(src)
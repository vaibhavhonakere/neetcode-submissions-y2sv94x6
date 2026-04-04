class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # minHeap containing distance of the (current height - prev height) 
        # as the first value of the minHeap
        # the second value can be the point it self. 
        # For example, minHeap = [(0, (0,0)), (0, (0,1)), (2, (1,0))]
        # visited hashSet = set() to keep track of the points we visited

        min_heap = [(0, (0,0))] # Running data structure to keep track of the minimum value and the point
        dirs = [[-1,0], [1,0], [0,1], [0,-1]]
        visited = set()
        ROWS = len(heights)
        COLS = len(heights[0])
        while min_heap:
            min_effort, point = heapq.heappop(min_heap)
            x,y = point
            if (x, y) in visited:
                continue
            if(x == ROWS - 1 and y == COLS - 1):
                return min_effort
            visited.add((x, y))
            for r,c in dirs:
                newX = x + r
                newY = y + c
                if((newX, newY) in visited or
                   0 > newX or 0 > newY or newX >= ROWS or newY >= COLS):
                   continue
                maxVal = max(min_effort, abs(heights[newX][newY] - heights[x][y]))
                heapq.heappush(min_heap, (maxVal, (newX, newY)))
        
        return -1
            



        
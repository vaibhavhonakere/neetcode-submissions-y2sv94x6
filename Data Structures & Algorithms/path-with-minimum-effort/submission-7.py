class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # BFS + minHeapApproach
        ROWS = len(heights)
        COLS = len(heights[0])
        queue = []
        queue.append((0,(0,0)))
        visit = set()
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]

        while(queue):
            weight, (x,y) = heapq.heappop(queue)
            if(x == ROWS - 1 and y == COLS - 1):
                return weight
            if((x,y) in visit):
                continue
            visit.add((x,y))
            for r,c in dirs:
                newX = r + x
                newY = c + y
                if((newX, newY) in visit or
                   newX >= ROWS or newY >= COLS or
                   newX < 0 or newY < 0):
                   continue
                
                newWeight = max(weight, abs(heights[x][y] - heights[newX][newY]))
                heapq.heappush(queue, (newWeight, (newX, newY)))
            


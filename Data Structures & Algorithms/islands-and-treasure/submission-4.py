class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque([])
        visit = set()
        for i in range(ROWS):
            for j in range(COLS):
                if(grid[i][j] == 0):
                    queue.append((i,j, 0))
        
        dirs = [[0,1], [1,0], [-1,0], [0, -1]]
        maxDist = float("-inf")
        while(queue):
            x,y, dist = queue.popleft()
            for r,c in dirs:
                newX = r + x
                newY = c + y
                if((newX, newY) in visit or 
                   newX >= ROWS or newY >= COLS or
                   newX < 0 or newY < 0 or grid[newX][newY] != 2147483647):
                   continue
                visit.add((newX, newY))
                # maxDist = max(maxDist, dist + 1)
                queue.append((newX, newY, dist + 1))
                grid[newX][newY] = dist + 1
        # return 

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        visit = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque([])

        for r in range(ROWS):
            for c in range(COLS):
                if(grid[r][c] == 0):
                    queue.append((r,c,0))
                    visit.add((r,c))
        

        while(queue):
            length = len(queue)
            for i in range(length):
                x1,y1, dist = queue.popleft()
                for x,y in dirs:
                    newX, newY = x + x1, y + y1
                    if(newX < 0 or newX >= ROWS or newY < 0 or 
                       newY >= COLS or grid[newX][newY] == -1 or
                       (newX, newY) in visit):
                       continue
                    grid[newX][newY] = min(grid[newX][newY], dist + 1)
                    queue.append((newX, newY, grid[newX][newY]))
                    visit.add((newX,newY))
                    print(queue)
            
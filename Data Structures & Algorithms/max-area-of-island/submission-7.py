class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        maxCount = 0
        count = 0
        def dfs(r,c):
            nonlocal count
            if(r < 0 or c < 0 or c >= COLS or 
                r >= ROWS or (r,c) in visit or grid[r][c] == 0):
                return
            
            visit.add((r,c))
            count += 1
            print(count)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return
        
        for i in range(ROWS):
            for j in range(COLS):
                if(grid[i][j] == 1 and (i,j) not in visit):
                    count = 0
                    dfs(i,j)
                    maxCount = max(maxCount, count)
        return maxCount
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        maxCount = 0
        def dfs(r,c):
            nonlocal count
            if(r < 0 or c < 0 or c >= COLS or 
                r >= ROWS or (r,c) in visit or grid[r][c] == 0):
                return 0
            
            visit.add((r,c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1)+ dfs(r, c - 1)
        
        for i in range(ROWS):
            for j in range(COLS):
                if(grid[i][j] == 1 and (i,j) not in visit):
                    count = 0
                    maxCount = max(maxCount, dfs(i,j))
        return maxCount
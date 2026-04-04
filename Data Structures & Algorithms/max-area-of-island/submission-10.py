class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(r, c):
            if((r,c) in visit or r >= ROWS or c >= COLS
             or 0 > r or 0 > c or grid[r][c] == 0):
                return 0
            visit.add((r,c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        ret = 0
        for i in range(ROWS):
            for j in range(COLS):
                if((i,j) not in visit and grid[i][j] == 1):
                    ret = max(ret, dfs(i,j))
        return ret
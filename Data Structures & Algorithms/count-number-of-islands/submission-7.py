class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(r, c):
            if((r,c) in visit or r >= ROWS or c >= COLS
             or 0 > r or 0 > c or grid[r][c] == "0"):
                return
            visit.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        ret = 0
        for i in range(ROWS):
            for j in range(COLS):
                if((i,j) not in visit and grid[i][j] == "1"):
                    ret += 1
                    dfs(i,j)
        return ret

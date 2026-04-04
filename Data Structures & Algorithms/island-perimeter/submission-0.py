class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        def dfs(r, c):
            if(r >= ROWS or c >= COLS or r < 0 or c < 0 or grid[r][c] == 0):
                return 1
            
            if((r,c) in visit):
                return 0
            
            visit.add((r,c))
            return dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        ret = 0
        for i in range(ROWS):
            for j in range(COLS):
                if(grid[i][j] == 1):
                    ret += dfs(i,j)

        return ret
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        count = 0
        def dfs(r,c):
            nonlocal count
            if(r < 0 or c < 0 or c >= COLS or 
                r >= ROWS or (r,c) in visit or grid[r][c] == "0"):
                return
            
            visit.add((r,c))
            # count += 1
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return
        
        for i in range(ROWS):
            for j in range(COLS):
                if(grid[i][j] == "1" and (i,j) not in visit):
                    dfs(i,j)
                    count += 1
        
        return count
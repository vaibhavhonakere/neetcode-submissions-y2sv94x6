class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()

        def dfs(r,c):
            if(r >= ROWS or c >= COLS or r < 0 or c < 0 or 
                grid[r][c] == 0 or (r,c) in visited):
                return 0
            
            visited.add((r,c))
            return 1 + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)

        max_area = 0
        for i in range(ROWS):
            for j in range(COLS):
                if(grid[i][j] == 1 and (i,j) not in visited):
                    max_area = max(max_area, dfs(i,j))
        
        return max_area
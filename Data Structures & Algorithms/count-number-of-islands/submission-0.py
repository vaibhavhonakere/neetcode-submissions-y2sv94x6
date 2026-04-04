class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M = len(grid[0])
        N = len(grid)
        seen = set()
        count = 0
        def dfs(i,j):
            if(i >= N or i < 0 or j < 0 or j >= M or grid[i][j] == "0" or (i,j) in seen):
                return
            seen.add((i,j))
            grid[i][j] = "0"
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == "1"):
                    dfs(i, j)
                    count += 1
        
        return count
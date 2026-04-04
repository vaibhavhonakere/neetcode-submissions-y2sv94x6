class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        dirs = [[0,1], [0, -1], [1,0], [-1, 0]]
        dp = {} # Cache for the row and column (r,c)

        def dfs(r,c, prev):
            if(r < 0 or r >= ROWS or
               c < 0 or c >= COLS or
               matrix[r][c] <= prev):
               return 0
            if((r,c) in dp):
                return dp[(r,c)]
            
            res = 1
            for x,y in dirs:
                res = max(res, 1 + dfs(r + x, c + y, matrix[r][c]))
            
            dp[(r,c)] = res
            return dp[(r,c)]
        
        maxVal = float("-inf")
        for i in range(ROWS):
            for j in range(COLS):
                maxVal = max(maxVal, dfs(i,j, -1))
        return maxVal

            

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # have sets being tracked for Pacific and Atlantic Oceans
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific_pts = set()
        atlantic_pts = set()
        # find the paths from the pacific/atlantic that is increasing from the boarders
        def dfs(r,c,visit,prev):
            if(r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visit or heights[r][c] < prev):
                return
            visit.add((r,c))
            prev = heights[r][c]
            dfs(r+1,c,visit,prev)
            dfs(r-1,c,visit,prev)
            dfs(r,c+1,visit,prev)
            dfs(r,c-1,visit,prev)
        
        for i in range(ROWS):
            for j in range(COLS):
                if(i == 0 or j == 0):
                    dfs(i,j,pacific_pts, float("-inf"))
                if(i == ROWS - 1 or j == COLS - 1):
                    dfs(i,j,atlantic_pts, float("-inf"))
                else:
                    continue
        
        intersected_pts = pacific_pts.intersection(atlantic_pts)
        ret = []
        for x,y in intersected_pts:
            ret.append([x,y])
        return ret
        
                

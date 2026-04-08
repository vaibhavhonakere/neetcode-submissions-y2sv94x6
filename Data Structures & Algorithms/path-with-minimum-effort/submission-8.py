class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        min_heap = [[0, (0,0)]]
        ROWS = len(heights)
        COLS = len(heights[0])
        dirs = [[-1,0], [1,0], [0,-1], [0,1]]
        visit = set()

        while(min_heap):
            # print("here")
            diff, (row, col) = heapq.heappop(min_heap)
            if(row == ROWS - 1 and col == COLS - 1):
                return diff
            if((row, col) in visit):
                continue 
            visit.add((row, col))
            for x,y in dirs:
                new_x = x + row
                new_y = y + col
                # print(new_x, new_y)
                if(0 > new_x or ROWS <= new_x or
                   0 > new_y or COLS <= new_y or
                   (new_x, new_y) in visit):
                   continue
                # print(new_x, new_y, diff, (row, col))
                
                heapq.heappush(
                    min_heap,
                    [
                        max(abs(heights[row][col] - heights[new_x][new_y]), diff),
                        (new_x, new_y)
                    ]
                )
            




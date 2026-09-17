class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # Find the treasure chests in the grid, and then from there do a 
        # multi source BFS from the adjacent positions and only check the INF values
        # and then build out the rest of the output
        N = len(grid)
        M = len(grid[0])
        queue = deque([])
        visited = set()
        dirs = [[-1,0], [1,0], [0,1], [0,-1]]

        for i in range(N):
            for j in range(M):
                if(grid[i][j] == 0):
                    queue.append((i,j))
        
        while(queue):
            r,c = queue.popleft()
            # if(r == N - 1 and c == N - 1):
            #     break 
            if((r,c) in visited):
                continue
            
            visited.add((r,c))

            for x,y in dirs:
                new_r, new_c = r + x, c + y
                if(0 > new_r or new_r >= N or 
                   0 > new_c or new_c >= M or
                   (new_r, new_c) in visited or 
                    grid[new_r][new_c] == -1):
                    continue
                # print(new_r, new_c)
                queue.append((new_r, new_c))
                grid[new_r][new_c] = min(grid[new_r][new_c], grid[r][c] + 1)
        
        

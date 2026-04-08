class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        visit = set()
        def dfs(r,c):
            if(r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visit or 
                board[r][c] == "X"):
                return
            visit.add((r,c))
            board[r][c] = "F"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for j in range(COLS):
            for i in [0, ROWS - 1]:
                if(board[i][j] == "O"):
                    dfs(i,j)
        
        for j in range(ROWS):
            for i in [0, COLS - 1]:
                if(board[j][i] == "O"):
                    dfs(j,i)
        
        for i in range(ROWS):
            for j in range(COLS):
                if(board[i][j] == "O"):
                    board[i][j] = "X"
                elif(board[i][j] == "F"):
                    board[i][j] = "O"

        


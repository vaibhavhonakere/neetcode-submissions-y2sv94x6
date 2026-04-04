class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        blockSet = defaultdict(set)
        ROWS = len(board)
        COLS = len(board[0])

        for i in range(ROWS):
            for j in range(COLS):
                if(board[i][j] == "."):
                    continue
                if(board[i][j] in rowSet[i] or
                   board[i][j] in colSet[j] or
                   board[i][j] in blockSet[(i//3, j// 3)]):
                   return False
                rowSet[i].add(board[i][j])
                colSet[j].add(board[i][j])
                blockSet[(i//3,j // 3)].add(board[i][j])
        return True
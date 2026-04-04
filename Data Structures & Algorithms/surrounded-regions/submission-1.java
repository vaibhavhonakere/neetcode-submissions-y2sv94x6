class Solution {
    private int ROWS;
    private int COLS;

    public void solve(char[][] board) {
        // Convert the O to F
        // Depth first search on the outer boarders and change F back to O
        // Traverse one more time to and check
        // if there is an F and change it to X

        this.ROWS = board.length;
        this.COLS = board[0].length;

        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                if(board[i][j] == 'O'){
                    board[i][j] = 'F';
                }
            }
        }
        HashSet<String> seen = new HashSet<>();
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                if((i == 0 || j == 0 || i == board.length - 1 || j == board[0].length - 1) && (board[i][j] == 'F')){
                    dfs(i,j,board,seen);
                }
            }
        }
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                if(board[i][j] == 'F'){
                    board[i][j] = 'X';
                }
            }
        }

    }
    private void dfs(int i, int j, char[][] board, HashSet<String> seen){
        if(i < 0 || j < 0 || i >= this.ROWS || j >= this.COLS || seen.contains(i +","+j) || board[i][j] == 'X'){
            return;
        }
        board[i][j] = 'O';
        seen.add(i+","+j);
        dfs(i + 1, j, board, seen);
        dfs(i - 1, j, board, seen);
        dfs(i, j + 1, board, seen);
        dfs(i, j - 1, board, seen);
        return;
    }
}

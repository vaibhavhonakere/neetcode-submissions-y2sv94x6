class Solution {
    HashSet<String> visited;
    private int rows;
    private int cols;
    private char[][] board;

    public boolean exist(char[][] board, String word) {
        this.visited = new HashSet<>();
        this.rows = board.length;
        this.cols = board[0].length;
        for(int i=0; i < rows; i++){
            for(int j=0; j < cols; j++){
                if(word.charAt(0) == board[i][j] && dfs(i,j,word, board, 0)){
                    return true;
                }
            }
        }
        //System.out.println(visited);
        return false;
    }
    private boolean dfs(int i, int j, String word, char[][] board, int str_index){
        if(str_index == word.length()){
            return true;
        }
        if(i >= rows || i < 0 || j < 0 || j >= cols || board[i][j] != word.charAt(str_index) || visited.contains(i + "," + j)){
            return false;
        }

        this.visited.add(i + "," + j);
        boolean check = dfs(i + 1, j, word, board, str_index + 1) ||
               dfs(i - 1, j, word, board, str_index + 1) ||
               dfs(i, j + 1, word, board, str_index + 1) ||
               dfs(i, j - 1, word, board, str_index + 1);
        this.visited.remove(i + "," + j);
        return (check);
    }
}

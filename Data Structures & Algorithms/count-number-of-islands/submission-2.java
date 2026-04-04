class Solution {
    private HashSet<String> visited;
    private int N;
    private int M;

    public int numIslands(char[][] grid) {
        this.visited = new HashSet<>();
        this.N = grid.length;
        this.M = grid[0].length;
        int count = 0;
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                //System.out.println(Character.toString(grid[i][j]).equals("1"));
                if(Character.toString(grid[i][j]).equals("1") && !this.visited.contains(i + "," + j)){
                    dfs(i,j,grid);
                    count += 1;
                }
            }
        }
        return count;

    }
    private void dfs(int i, int j, char[][] board){
        if(i < 0 || j < 0 || i >= this.N 
           || j >= this.M || this.visited.contains(i + "," + j) ||
           Character.toString(board[i][j]).equals("0")){
            return;
        }
        this.visited.add(i + "," + j);
        dfs(i + 1, j, board);
        dfs(i - 1, j, board);
        dfs(i, j + 1, board);
        dfs(i, j - 1, board);
        return;
    }
}

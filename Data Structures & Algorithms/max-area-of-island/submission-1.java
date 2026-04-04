class Solution {
    private HashSet<String> visited;
    private int N;
    private int M;
    private int sizeOfIsland = 0;

    public int maxAreaOfIsland(int[][] grid) {
        this.visited = new HashSet<>();
        this.N = grid.length;
        this.M = grid[0].length;
        int maxSize = 0;
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                //System.out.println(Character.toString(grid[i][j]).equals("1"));
                if(grid[i][j] == 1 && !this.visited.contains(i + "," + j)){
                    dfs(i,j,grid);
                    maxSize = Math.max(maxSize,this.sizeOfIsland);
                    this.sizeOfIsland = 0;
                }
            }
        }
        return maxSize;

    }
    private void dfs(int i, int j, int[][] board){
        if(i < 0 || j < 0 || i >= this.N 
           || j >= this.M || this.visited.contains(i + "," + j) ||
           board[i][j] == 0){
            return;
        }
        this.visited.add(i + "," + j);
        this.sizeOfIsland += 1;
        dfs(i + 1, j, board);
        dfs(i - 1, j, board);
        dfs(i, j + 1, board);
        dfs(i, j - 1, board);
        return;
    }
}

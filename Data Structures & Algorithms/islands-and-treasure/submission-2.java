class Solution {
    public void islandsAndTreasure(int[][] grid) {
        Queue<int[]> q = new LinkedList<>();
        int [][] dirs = {{0,1},{1,0},{0,-1},{-1,0}};
        HashSet<String> visited = new HashSet<>();
        int m = grid.length;
        int n = grid[0].length;
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(grid[i][j] == 0){
                    q.add(new int[]{i,j,0});
                }
            }
        }
        while(!q.isEmpty()){
            int[] point = q.poll();
            int x = point[0];
            int y = point[1];
            int val = point[2];
            visited.add(x + "," + y);
            for(int i=0; i < 4; i++){
                int[] d = dirs[i];
                int distX = x + d[0];
                int distY = y + d[1];
                if(distX < 0 || distY < 0 || distX >= m || distY >= n 
                   || visited.contains(distX + "," + distY) || grid[distX][distY] == -1){
                    continue;
                }
                grid[distX][distY] = Math.min(grid[distX][distY], val + 1);
                q.add(new int[]{distX,distY, val + 1});
            }
        }

    }
}

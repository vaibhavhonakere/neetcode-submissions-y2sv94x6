class Solution {
    public int orangesRotting(int[][] grid) {
        Queue<int[]> q = new LinkedList<>();
        int freshFruit = 0;
        int [][] dirs = {{0,1},{1,0},{0,-1},{-1,0}};
        HashSet<String> visited = new HashSet<>();
        int m = grid.length;
        int n = grid[0].length;
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(grid[i][j] == 2){
                    q.add(new int[]{i,j,0});
                    visited.add(i + "," + j);
                }else if(grid[i][j] == 1){
                    freshFruit += 1;
                }
            }
        }
        int val = 0;
        while(!q.isEmpty()){
            int[] point = q.poll();
            int x = point[0];
            int y = point[1];
            val = point[2];
            System.out.println("The point " + x + ":" + y + " First : " + val);
            for(int i=0; i < 4; i++){
                int[] d = dirs[i];
                int distX = x + d[0];
                int distY = y + d[1];
                if(distX < 0 || distY < 0 || distX >= m || distY >= n 
                   || visited.contains(distX + "," + distY) || grid[distX][distY] == 0){
                    continue;
                }
                visited.add(distX + "," + distY);
                //grid[distX][distY] = 2;
                q.add(new int[]{distX,distY, val + 1});
                freshFruit -= 1;
                // if(grid[distX][distY] == 1){
                //     freshFruit -= 1;
                // }
            }
        }
        return (freshFruit == 0) ? val : -1;
    }
}

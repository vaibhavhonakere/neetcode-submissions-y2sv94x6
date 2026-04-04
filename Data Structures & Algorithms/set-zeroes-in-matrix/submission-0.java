class Solution {
    public void setZeroes(int[][] matrix) {
        Queue<int[]> queue = new LinkedList<>();
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[0].length; j++){
                if(matrix[i][j] == 0){
                    queue.add(new int[]{i,j});
                }
            }
        }
        while(!queue.isEmpty()){
            int[] p = queue.poll();
            for(int i = 0; i < matrix.length; i++){
                matrix[i][p[1]] = 0;
            }
            for(int i = 0; i < matrix[0].length; i++){
                matrix[p[0]][i] = 0;
            }
        }
    }
}

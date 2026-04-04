class Solution {
    public void setZeroes(int[][] matrix) {
        boolean topRow = false;
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[0].length; j++){
                if(matrix[i][j] == 0){
                    matrix[0][j] = 0;
                    if(i > 0){
                        matrix[i][0] = 0;
                    }else{
                        topRow = true;
                    }

                }
            }
        }
        //System.out.println("first");
        for(int i = 1; i < matrix.length; i++){
            for(int j = 1; j < matrix[0].length; j++){
                if(matrix[i][0] == 0 || matrix[0][j] == 0){
                    matrix[i][j] = 0;
                }
            }
            //System.out.println("here");
        }
        for(int i = 0; i < matrix.length; i++){

            for(int j = 0; j < matrix[0].length; j++){
                System.out.print(matrix[i][j]);
            }
            System.out.print("\n");
        }
        if(matrix[0][0] == 0){
            for(int r=0; r < matrix.length; r++){
                matrix[r][0] = 0;
            }
        }
        //System.out.println("third");
        if(topRow){
            for(int c=0; c < matrix[0].length; c++){
                matrix[0][c] = 0;
            }
        }

        // Queue<int[]> queue = new LinkedList<>();
        // for(int i = 0; i < matrix.length; i++){
        //     for(int j = 0; j < matrix[0].length; j++){
        //         if(matrix[i][j] == 0){
        //             queue.add(new int[]{i,j});
        //         }
        //     }
        // }
        // while(!queue.isEmpty()){
        //     int[] p = queue.poll();
        //     for(int i = 0; i < matrix.length; i++){
        //         matrix[i][p[1]] = 0;
        //     }
        //     for(int i = 0; i < matrix[0].length; i++){
        //         matrix[p[0]][i] = 0;
        //     }
        // }
    }
}

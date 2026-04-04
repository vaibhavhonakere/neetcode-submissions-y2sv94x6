class Solution {
    public void rotate(int[][] matrix) {
        int left = 0;
        int right = matrix.length - 1;

        while(left < right){
            for(int i = 0; i < (right - left); i++){
                // save top left
                // assign top left with bottom left
                // assign bottom left with bottom right
                // assign bottom right with top right
                // assign top right with top left

                int top = left;
                int bot = right;

                int temp = matrix[top][left + i];

                matrix[top][left + i] = matrix[bot - i][left];

                matrix[bot - i][left] = matrix[bot][right - i];

                matrix[bot][right - i] = matrix[top + i][right];

                matrix[top + i][right] = temp;
            }
            left += 1;
            right -= 1;
        }
    }
}

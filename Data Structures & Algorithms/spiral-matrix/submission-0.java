class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> ret = new ArrayList<>();
        int left = 0, right = matrix[0].length;
        int top = 0, bot = matrix.length;

        while(left < right && top < bot){
            for(int i = left; i < right; i++){
                ret.add(matrix[top][i]);
            }
            top += 1;
            for(int i = top; i < bot; i++){
                ret.add(matrix[i][right - 1]);
            }
            right -= 1;

            if(!(left < right && top < bot)) {
                break;
            }

            for(int i = right - 1; i >= left; i--){
                ret.add(matrix[bot - 1][i]);
            }
            bot -= 1;
            for(int i = bot - 1; i >= top; i--){
                ret.add(matrix[i][left]);
            }
            left += 1;
        }
        return ret;
    }
}
class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        let left = 0;
        let right = matrix.length - 1;
        let mid = 0;
        while(left <= right){
            mid = left + Math.floor((right - left) / 2);
            if(matrix[mid][0] > target){
                right = mid - 1
            }else if(matrix[mid][matrix[0].length - 1] < target){
                left = mid + 1
            }else{
                break
            }
        }
        console.log(mid)

        left = 0
        right = matrix[mid].length - 1;
        while(left <= right){
            let m = left + Math.floor((right - left) / 2);
            if(matrix[mid][m] < target){
                left = m + 1
            }else if(matrix[mid][m] > target){
                right = m - 1
            }else{
                return true;
            }
        }
        return false;
    }
}

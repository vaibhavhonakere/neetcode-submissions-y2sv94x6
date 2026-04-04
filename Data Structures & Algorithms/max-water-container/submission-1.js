class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let left = 0;
        let right = heights.length - 1;
        let ret = Number.MIN_SAFE_INTEGER;
        // console.log("first " + ret)
        while(left < right){
            if(heights[left] < heights[right]){
                ret = Math.max(heights[left] * (right - left), ret);
                left++;
            }else{
                ret = Math.max(heights[right] * (right - left), ret);
                right--;
            }
            // console.log(ret)
        }
        return ret;
    }
}

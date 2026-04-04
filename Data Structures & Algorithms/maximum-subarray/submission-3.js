class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxSubArray(nums) {
        let maxVal = Number.MIN_SAFE_INTEGER;
        let ret = 0
        for(let n of nums){
            ret += n
            maxVal = Math.max(ret, maxVal)
            if(ret < 0){
                ret = 0
            }
        }
        return maxVal
    }
}

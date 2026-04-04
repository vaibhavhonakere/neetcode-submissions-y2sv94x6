class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    lengthOfLIS(nums) {
        let dp = Array(nums.length).fill(1)
        let ret = 0
        for(let i = nums.length - 1; i >= 0; i--){
            let res = 1;
            for(let j = i + 1; j < nums.length; j++){
                if(nums[i] < nums[j]){
                    // res = Math.max(res, Math.max(dp[i], dp[j]) + 1)
                    // // OR
                    dp[i] = Math.max(dp[i], dp[j] + 1)
                }
            }
            // dp[i] = res
            ret = Math.max(dp[i], ret)
        }   
        return ret
    }
}

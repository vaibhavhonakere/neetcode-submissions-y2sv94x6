class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxProduct(nums) {
        let res = nums[0]
        let curMin = 1
        let curMax = 1
        for(let n of nums){
            let tmp = curMax * n
            curMax = Math.max(Math.max(curMax * n, curMin * n), n)
            curMin = Math.min(Math.min(tmp, curMin * n), n)
            res = Math.max(res, curMax, n)
        }
        return res

    }
}

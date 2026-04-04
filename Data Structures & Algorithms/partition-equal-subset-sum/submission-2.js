class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    canPartition(nums) {
        let sumVal = 0
        for(let i = 0; i < nums.length; i++){
            sumVal += nums[i]
        }
        if(sumVal % 2 !== 0){
            return false
        }
        let subTarget = sumVal / 2
        const dfs = ((i, subSum) => {
            if(subSum === subTarget){
                return true
            }else if(subSum > subTarget || i > nums.length){
                return false
            }
            return dfs(i + 1, subSum + nums[i]) || dfs(i + 1, subSum)
        })
        return dfs(0, 0)

    }
}

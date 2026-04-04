class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @returns {number[][]}
     */
    combinationSum(nums, target) {
        let ret = []
        const dfs = ((i, subset, sumVal) =>{
            if(sumVal === target){
                ret.push([...subset])
                return
            }
            if(sumVal > target || i == nums.length){
                return
            }
            subset.push(nums[i])
            dfs(i, subset, sumVal + nums[i])
            subset.pop()
            dfs(i + 1, subset, sumVal)
        })
        dfs(0, [], 0)
        return ret

    }
}

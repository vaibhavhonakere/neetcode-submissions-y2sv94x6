class Solution {
    /**
     * @param {number[]} candidates
     * @param {number} target
     * @return {number[][]}
     */
    combinationSum2(candidates, target) {
        candidates.sort()
        let ret = []
        let nums = candidates
        const dfs = ((i, subset, sumVal) => {
            if(sumVal === target){
                ret.push([...subset])
                return
            }
            if(sumVal > target || i == nums.length){
                return
            }
            subset.push(nums[i])
            dfs(i + 1, subset, sumVal + nums[i])
            subset.pop()
            while(i + 1 < nums.length && nums[i] == nums[i+1]){
                i++
            }
            dfs(i + 1, subset, sumVal)
        })
        dfs(0, [], 0)
        return ret
    }
}

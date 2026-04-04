class Solution {
    /**
     * @param {number[]} cost
     * @return {number}
     */
    minCostClimbingStairs(cost) {
        let minVal = Number.MAX_SAFE_INTEGER
        const dfs = ((i, c) => {
            if(i >= cost.length){
                minVal = Math.min(minVal, c)
                return 1
            }
            dfs(i + 1, c + cost[i])
            dfs(i + 2, c + cost[i])
        })
        dfs(0, 0)
        dfs(1,0)
        return minVal
    }
}

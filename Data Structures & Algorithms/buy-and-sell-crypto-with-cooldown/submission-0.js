class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {

        let cache = new Map() // (index, buy or sell boolean)

        const dfs = ((i, buying) => {
            if(i >= prices.length){
                return 0
            }
            if(cache.has(`${i},${buying}`)){
                return cache.get(`${i},${buying}`)
            }
            let buy = 0, cooldown = 0;
            if(buying){
                buy = dfs(i + 1, !buying) - prices[i]
                cooldown = dfs(i + 1, buying)
                cache.set(`${i},${buying}`, Math.max(buy, cooldown))
            }else{
                buy = dfs(i + 2, !buying) + prices[i]
                cooldown = dfs(i + 1, buying)
                cache.set(`${i},${buying}`, Math.max(buy, cooldown))
            }
            return cache.get(`${i},${buying}`)
        })
        return dfs(0, true)
    }
}

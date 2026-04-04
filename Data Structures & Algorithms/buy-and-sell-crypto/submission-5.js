class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        if(prices.length == 1){
            return 0
        }
        let maxProfit = 0;
        let r = 1
        let i = 0
        while(r < prices.length){
            if(prices[i] < prices[r]){
                maxProfit = Math.max(maxProfit, prices[r] - prices[i])
            }else{
                i = r;
            }
            r++;
        }
        return maxProfit;
    }
}

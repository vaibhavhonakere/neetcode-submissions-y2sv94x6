class Solution {
    public int maxProfit(int[] prices) {
        if(prices.length == 1){
            return 0;
        }
        int maxVal = 0;
        int left = 0;
        int right = 1;
        while(right < prices.length){
            if(prices[left] <= prices[right]){
                maxVal = Math.max(maxVal, prices[right] - prices[left]);
            }else{
                left = right;
            }
            right++;
        }
        return maxVal;
    }
}

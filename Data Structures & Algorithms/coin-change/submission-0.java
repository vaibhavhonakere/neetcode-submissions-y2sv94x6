class Solution {
    private int minVal;
    private int amount;
    public int coinChange(int[] coins, int amount) {
        this.minVal = Integer.MAX_VALUE;
        this.amount = amount;
        dfs(0, coins, 0, 0);
        if(minVal == Integer.MAX_VALUE){
            return -1;
        }
        return minVal;
    }
    private void dfs(int index, int[] coins, int ways, int currSum){
        if(currSum == amount){
            //System.out.println("The ways " + ways + " , The index " + index);
            minVal = Math.min(minVal, ways);
            return;
        }
        if(index >= coins.length || currSum > amount){
            return;
        }
        dfs(index, coins, ways + 1, currSum + coins[index]);

        dfs(index + 1, coins, ways, currSum);
    }
}

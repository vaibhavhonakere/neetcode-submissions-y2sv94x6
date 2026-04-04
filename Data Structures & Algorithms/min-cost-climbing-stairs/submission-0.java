class Solution {
    private HashMap<Integer, Integer> map;
    public int minCostClimbingStairs(int[] cost) {
        int[] temp = new int[cost.length + 1];
        for(int i = 0; i < temp.length; i++){
            if(i == temp.length - 1){
                temp[i] = 0;
            }else{
                temp[i] = cost[i];
            }
        }
        for(int i = temp.length - 3; i >= 0 ; i--){
            temp[i] += Math.min(temp[i+2], temp[i+1]);
        }
        return Math.min(temp[0], temp[1]);
        //return Math.min(dfs(0, cost[0], cost), dfs(1, cost[1], cost));
    }

}

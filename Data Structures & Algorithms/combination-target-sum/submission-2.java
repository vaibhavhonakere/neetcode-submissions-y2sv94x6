class Solution {
    private List<List<Integer>> ret;
    private int length;
    private int target;

    public List<List<Integer>> combinationSum(int[] nums, int target) {
        this.ret = new ArrayList<>();
        this.length = nums.length;
        this.target = target;
        dfs(0, new ArrayList<>(), nums, 0);
        return ret; 
    }
    private void dfs(int index, List<Integer>subset, int[]nums, int sumVal){
        if(sumVal == target){
            ret.add(new ArrayList<>(subset));
            return;
        }
        if(sumVal > target || index == length){
            return;
        }
        for(int i = index; i < nums.length;i++){
            subset.add(nums[i]);
            dfs(i, subset, nums, sumVal + nums[i]);
            subset.remove(subset.size() - 1);
        }
        // dfs(index + 1, subset, nums, sumVal);
        return;
    }
}

class Solution {
    private List<List<Integer>> ret;
    private int length;
    public List<List<Integer>> subsets(int[] nums) {
        this.ret = new ArrayList<>();
        this.length = nums.length;
        dfs(0, new ArrayList<>(), nums);
        return ret; 
    }
    private void dfs(int index, List<Integer>subset, int[]nums){
        if(index == length){
            ret.add(new ArrayList<>(subset));
            return;
        }
        subset.add(nums[index]);
        dfs(index + 1, subset, nums);
        subset.remove(subset.size() - 1);
        dfs(index + 1, subset, nums);
        return;
    }
}

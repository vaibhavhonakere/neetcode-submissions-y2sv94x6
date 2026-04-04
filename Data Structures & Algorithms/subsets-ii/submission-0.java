class Solution {
    private List<List<Integer>> ret;
    private int length;
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        this.ret = new ArrayList<>();
        this.length = nums.length;
        Arrays.sort(nums);
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
        while(index + 1 < nums.length && nums[index] == nums[index+1]){
            index++;
        }
        dfs(index + 1, subset, nums);
        return;
    }
}

class Solution {
    public int singleNumber(int[] nums) {
        // XOR --> 1 1 == 0
        //     --> 1 0 == 1
        //     --> 0 1 == 1
        //     --> 0 0 == 0

        int ret = 0;
        for(int n : nums){
            ret = ret ^ n;
        }
        return ret;
    }
}

class Solution {
    public int maxSubArray(int[] nums) {
        int largest = Integer.MIN_VALUE;
        int curr = 0;
        for(int n: nums){
            if(curr < 0){
                //largest = Math.max(n, largest);
                curr = 0;
            }
            curr += n;
            largest = Math.max(curr, largest);
        }
        return largest;
    }
}

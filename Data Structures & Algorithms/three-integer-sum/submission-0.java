class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> ret = new ArrayList<>();
        for(int i = 0; i < nums.length - 2; i++){
            if(i == 0 || (i > 0 && nums[i] != nums[i-1])){
                int original = nums[i];
                int left = i + 1;
                int right = nums.length - 1;
                while(left < right){
                    //System.out.println("The left " + nums[left] + " The right " + nums[right] + " The original "+ original);
                    if(nums[left] + nums[right] + original == 0){
                        ret.add(List.of(nums[i], nums[left], nums[right]));
                        while (left < right && nums[left] == nums[left + 1]) {
                            left++;
                        }
                        while (left < right && nums[right] == nums[right - 1]) {
                            right--;
                        }
                        left++;
                        right--;
                    }else if(nums[left] + nums[right] + original > 0){
                        right--;
                    }else{
                        left++;
                    }
                }
            }
        }
        return ret;
    }
}

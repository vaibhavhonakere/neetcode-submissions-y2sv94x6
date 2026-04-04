class Solution {
    public int findKthLargest(int[] nums, int k) {
        k = nums.length - k;
        int left = 0;
        int right = nums.length - 1;
        int pivot = 0;
        while(left <= right){
            pivot = quickSelect(nums, left, right);
            if(pivot > k){
                right = pivot - 1;
            }else if(pivot < k){
                left = pivot + 1;
            }else{
                break;
            }
        }
        return nums[pivot];
    }
    public int quickSelect(int[] arr, int left, int right){
        int pivot = arr[right];
        int fill = left;
        for(int i = left; i < right; i++){
            if(arr[i] <= pivot){
                int temp = arr[fill];
                arr[fill] = arr[i];
                arr[i] = temp;
                fill += 1;
            }
        }
        int temp_2 = arr[right];
        arr[right] = arr[fill];
        arr[fill] = temp_2;
        return fill;
    }
}

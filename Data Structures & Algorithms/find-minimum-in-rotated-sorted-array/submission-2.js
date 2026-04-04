class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
        let l = 0
        let r = nums.length - 1;
        let minVal = 1001
        while(l < r){
            let mid = Math.floor((l + r) / 2)
            minVal = Math.min(minVal, nums[mid])
            if(nums[mid] > nums[r]){
                l = mid + 1
            }else if(nums[mid] < nums[l]){
                r = mid - 1
            }else{
                break
            }
        }
        return Math.min(minVal, nums[l])
    }
}

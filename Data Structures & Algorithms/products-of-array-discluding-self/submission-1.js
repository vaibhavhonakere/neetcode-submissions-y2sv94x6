class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
//       [1,2,4,6]
//       [1,2,8,48]
//       [1,24,12,8]
//       [48,24,12,8]
  
        let store = [];
        let multiplier = 1;
        for(let i = 0; i < nums.length; i++){
            multiplier = multiplier * nums[i];
            store.push(multiplier);
        }
        let val = 1;
        for(let i = store.length - 2; i >= 0; i--){
            store[i + 1] = val * store[i];
            val *= nums[i + 1]
        }
        store[0] = val;
        return store

    }
}

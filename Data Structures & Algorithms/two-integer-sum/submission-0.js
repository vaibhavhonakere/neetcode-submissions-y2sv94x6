class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const cache = {}
        for(let i = 0; i < nums.length; i++){
            if(target - nums[i] in cache){
                return [i, cache[target - nums[i]]];
            }
            cache[nums[i]] = i;
        }
        return [];
    }
}

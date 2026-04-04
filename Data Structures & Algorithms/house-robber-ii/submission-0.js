class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    rob_2(nums) {
        let rob1 = 0;
        let rob2 = 0;

        for (const num of nums) {
            const temp = Math.max(num + rob1, rob2);
            rob1 = rob2;
            rob2 = temp;
        }
        return rob2;
    }
    rob(nums) {
        return Math.max(nums[0], this.rob_2(nums.slice(1)), this.rob_2(nums.slice(0, nums.length - 1)))
    }
}

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_min = 0
        cur_max = 0
        global_max = nums[0]
        global_min = nums[0]
        # run
        for n in nums:
            cur_max = max(cur_max + n, n)
            cur_min = min(cur_min + n, n)
            global_max = max(global_max, cur_max)
            global_min = min(global_min, cur_min)
        
        return max(sum(nums) - global_min, global_max) if(global_max > 0) else global_max



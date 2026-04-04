class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum_count = 0
        min_length = float("inf")
        for right in range(len(nums)):
            sum_count += nums[right]

            while(sum_count >= target):
                min_length = min(right - left + 1, min_length)
                sum_count -= nums[left]
                left += 1
            
        
        return 0 if(min_length == float("inf")) else min_length



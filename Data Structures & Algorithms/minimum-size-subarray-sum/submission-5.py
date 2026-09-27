class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        minimal_length = float("inf")

        cur_sum = 0

        for right in range(len(nums)):
            cur_sum += nums[right]
            # print(cur_sum, target)
            while(cur_sum >= target):
                minimal_length = min(minimal_length, right - left + 1)
                cur_sum -= nums[left]
                left += 1
            
            # if(cur_sum == target):
            #     minimal_length = min(minimal_length, right - left + 1)
        
        return 0 if(minimal_length == float("inf")) else minimal_length

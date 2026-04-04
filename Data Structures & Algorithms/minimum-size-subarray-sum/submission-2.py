class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float("inf")
        left = 0
        targetSum = 0
        for right in range(len(nums)):
            targetSum += nums[right]
            while(targetSum >= target):
                minLength = min(minLength, right - left + 1)
                targetSum -= nums[left]
                left += 1
        
        return 0 if(minLength == float("inf")) else minLength


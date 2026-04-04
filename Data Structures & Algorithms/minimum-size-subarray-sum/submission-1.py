class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minLength = len(nums) + 1
        sumV = 0
        for r in range(len(nums)):
            sumV += nums[r]
            while(sumV >= target):
                minLength = min(minLength, r - l + 1)
                sumV -= nums[l]
                l += 1
    
        return minLength if(minLength != len(nums) + 1) else 0
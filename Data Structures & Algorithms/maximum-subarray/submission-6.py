class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largestSum = 0
        maxVal = float("-inf")
        for n in nums:
            largestSum += n
            maxVal = max(maxVal, largestSum)
            if(largestSum < 0):
                largestSum = 0
        
        return maxVal
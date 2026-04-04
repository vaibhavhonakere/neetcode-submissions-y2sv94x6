class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       currSum = 0
       maxLength = float("-inf")
       for n in nums:
          currSum += n
          maxLength = max(maxLength, currSum)
          if(currSum < 0):
            currSum = 0

       return maxLength
        
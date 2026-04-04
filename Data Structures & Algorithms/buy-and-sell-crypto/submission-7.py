class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nums = prices
        l = 0
        r = 1
        maxVal = 0
        while(r < len(prices)):
            if(nums[l] < nums[r]):
                maxVal = max(maxVal, nums[r] - nums[l])
            else:
                l = r
            r += 1
        
        return maxVal
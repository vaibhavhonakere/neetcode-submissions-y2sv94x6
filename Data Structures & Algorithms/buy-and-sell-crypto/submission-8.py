class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_val = 0
        while(right < len(prices)):
            if(prices[left] > prices[right]):
                left = right
            else:
                max_val = max(max_val, prices[right] - prices[left])

            right += 1
        
        return max_val
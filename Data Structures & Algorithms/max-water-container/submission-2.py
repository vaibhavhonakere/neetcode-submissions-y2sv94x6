class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0

        right = len(heights) - 1
        nums = heights
        max_val = float("-inf")
        while(left <= right):
            height = min(nums[left], nums[right])
            max_val = max(max_val, height * (right - left))

            if(nums[right] > nums[left]):
                left += 1
            else:
                right -= 1
        
        return max_val
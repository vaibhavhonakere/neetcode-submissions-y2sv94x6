class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i, left = 0, 0
        right = len(nums) - 1
        length = len(nums)
        while(i <= right):
            if(nums[i] == 0):
                tmp = nums[left]
                nums[left] = nums[i]
                nums[i] = tmp
                left += 1
            elif(nums[i] == 2):
                print("first ", nums, i, right)
                tmp = nums[right]
                nums[right] = nums[i]
                nums[i] = tmp
                right -= 1
                print("second ", nums, i, right)
                i -= 1
            i += 1
        
        
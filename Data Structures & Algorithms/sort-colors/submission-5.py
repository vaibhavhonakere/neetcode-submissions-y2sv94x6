class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        beg = 0
        end = len(nums) - 1
        while(i <= end):
            if(nums[i] == 0):
                nums[beg], nums[i] = nums[i], nums[beg]
                beg += 1
            elif(nums[i] == 2):
                nums[end], nums[i] = nums[i], nums[end]
                end -= 1
                i -= 1

            i += 1
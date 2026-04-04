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
                tmp = nums[beg]
                nums[beg] = nums[i]
                nums[i] = tmp
                beg += 1
                # i -= 1
            elif(nums[i] == 2):
                tmp = nums[end]
                nums[end] = nums[i]
                nums[i] = tmp
                end -= 1
                i -= 1

            i += 1
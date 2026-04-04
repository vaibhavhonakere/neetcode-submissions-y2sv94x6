class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        beg = 0
        for i in range(len(nums)):
            if(i > 0 and nums[i] != nums[i - 1]):
                nums[beg + 1] = nums[i]
                beg += 1

        return beg + 1
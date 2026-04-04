class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        beg = 1

        for i in range(1, len(nums)):
            if(nums[i] != nums[i - 1]):
                nums[beg] = nums[i]
                beg += 1
        return beg
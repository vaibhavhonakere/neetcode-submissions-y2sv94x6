class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        all_nums = set(nums)
        max_count = 1
        for n in nums:
            if(n - 1 not in all_nums):
                start = 0
                while(start + n in all_nums):
                    # print(start + n)
                    max_count = max(max_count, start + 1)
                    start += 1
        
        return max_count
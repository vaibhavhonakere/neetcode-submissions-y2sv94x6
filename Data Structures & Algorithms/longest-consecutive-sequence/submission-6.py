class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        all_nums = set(nums)
        max_count = 1
        for n in nums:
            count = 1
            test_num = n
            while(test_num - 1 in all_nums):
                count += 1
                max_count = max(max_count, count)
                test_num -= 1
        
        return 0 if(max_count == float("-inf")) else max_count
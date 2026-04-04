class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums) < 2):
            return nums[0]
        cache = {}
        def dfs(i):
            if(i >= len(nums)):
                return 0
            
            if(i in cache):
                return cache[i]
            
            cache[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return cache[i]
        
        n = nums.pop(0)
        first = dfs(0)
        nums.insert(0, n)

        cache = {}
        nums.pop()
        second = dfs(0)
        return max(first, second)
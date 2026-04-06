class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        nums = candidates
        nums.sort()
        def backtrack(i, subset, subset_sum):
            nonlocal res
            if(subset_sum == target):
                res.append(subset.copy())
                return
            if(subset_sum > target or i >= len(nums)):
                return
    
            subset.append(nums[i])
            backtrack(i + 1, subset, subset_sum + nums[i])
            subset.pop()
            while(i + 1 < len(nums) and nums[i] == nums[i+1]):
                i += 1
            backtrack(i + 1, subset, subset_sum)
        
        backtrack(0, [], 0)
        return res
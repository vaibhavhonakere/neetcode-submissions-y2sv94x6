class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, subset, subset_sum):
            nonlocal res
            if(subset_sum == target):
                res.append(subset.copy())
                return
            if(subset_sum > target or i >= len(nums)):
                return
    
            subset.append(nums[i])
            backtrack(i, subset, subset_sum + nums[i])
            subset.pop()
            backtrack(i + 1, subset, subset_sum)
        
        backtrack(0, [], 0)
        return res
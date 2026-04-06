class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def backtrack(i, subset):
            nonlocal res
            if(i >= len(nums)):
                res += subset
                return
    
            subset ^= nums[i]
            backtrack(i + 1, subset)
            subset ^= nums[i]
            backtrack(i + 1, subset)
        
        backtrack(0, 0)
        return res

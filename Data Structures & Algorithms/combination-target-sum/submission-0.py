class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ret = []

        def dfs(i, subset, sumVal):
            if(sumVal == target):
                ret.append(subset[::])
                return
            if(sumVal > target or i == len(nums)): return 
            
            subset.append(nums[i])
            dfs(i, subset, sumVal + nums[i])
            subset.pop()
            dfs(i+1, subset, sumVal)
        
        dfs(0, [], 0)
        return ret
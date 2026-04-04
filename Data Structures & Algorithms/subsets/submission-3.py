class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def dfs(i, subset):
            if(i == len(nums)):
                ret.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()
            dfs(i + 1, subset)
        
        dfs(0, [])
        return ret
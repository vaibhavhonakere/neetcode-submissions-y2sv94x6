class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        def dfs(i, subset, subSum):
            if(subSum == target):
                ret.append(subset.copy())
                return
            if(i == len(nums) or subSum > target):
                return
            
            subset.append(nums[i])
            dfs(i, subset, subSum + nums[i])
            subset.pop()
            dfs(i + 1, subset, subSum)
        
        dfs(0, [], 0)
        return ret
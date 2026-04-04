class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        nums = candidates
        nums.sort()
        def dfs(i, subset, subSum):
            if(subSum == target):
                ret.append(subset.copy())
                return
            if(i == len(nums) or subSum > target):
                return
            
            subset.append(nums[i])
            dfs(i + 1, subset, subSum + nums[i])
            subset.pop()

            while(i + 1 < len(nums) and nums[i] == nums[i + 1]):
                i += 1
            dfs(i + 1, subset, subSum)
        
        dfs(0, [], 0)
        return ret
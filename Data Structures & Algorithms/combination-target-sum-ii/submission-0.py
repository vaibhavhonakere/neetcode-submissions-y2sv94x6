class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ret = []
        def dfs(i, subset, sumVal):
            if(sumVal == target):
                ret.append(subset[::])
                return
            if(i == len(candidates)):
                return
            if(sumVal > target):
                return
            
            subset.append(candidates[i])
            dfs(i + 1, subset, sumVal + candidates[i])
            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, subset, sumVal)
        
        dfs(0, [], 0)
        return ret

        
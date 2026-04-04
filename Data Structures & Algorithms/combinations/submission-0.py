class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        def dfs(i, subset):
            if(len(subset) == k):
                ret.append(subset.copy())
                return
            
            if(i > n):
                return

            subset.append(i)
            dfs(i + 1, subset)
            subset.pop()
            dfs(i + 1, subset)
        
        dfs(1, [])
        return ret
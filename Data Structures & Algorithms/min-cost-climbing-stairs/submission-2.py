class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        n = len(cost)
        def dfs(i):
            if(i == n):
                return 0
            if(i > n):
                return 100
            if(i in cache):
                return cache[i]
            
            cache[i] = cost[i] + min(dfs(i + 2),dfs(i + 1))
            return cache[i]
        
        return min(dfs(0), dfs(1))
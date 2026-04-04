class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(i):
            if(i == n):
                return 1
            if(i > n):
                return 0
            if(i in cache):
                return cache[i]
            
            return dfs(i + 2) + dfs(i + 1)
        
        return dfs(0)

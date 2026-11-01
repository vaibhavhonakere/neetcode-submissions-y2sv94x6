class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # tracking state
        n = len(cost)
        dp = {} # the step: number of ways

        # def dfs(i):
        #     if(i in dp):
        #         return dp[i]
        #     if(i >= n):
        #         return 0 
        #     dp[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
        #     return dp[i]
        
        # return min(dfs(0), dfs(1))

        def dfs(index, c):
            if((index, c) in dp):
                return dp[(index, c)] 
            if(index > n):
                return float("inf")
            if(index == n):
                return c
            
            first = dfs(index + 1, cost[index] + c)
            second = dfs(index + 2, cost[index] + c)
            dp[(index, c)] = min(first, second)
            return dp[(index, c)]

        return min(dfs(0, 0), dfs(1, 0))
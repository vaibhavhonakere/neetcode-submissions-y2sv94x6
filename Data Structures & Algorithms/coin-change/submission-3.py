class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp = {}
        # def dfs(change):
        #     if(change in dp):
        #         return dp[change]
            
        #     if(change == amount):
        #         return 0
            
        #     count = 1e9
        #     for c in coins:
        #         if(c + change <= amount):
        #             count = min(count, 1 + dfs(c + change))
            
        #     dp[change] = count
        #     return dp[change]
        
        # minCoins = dfs(0)
        # return -1 if minCoins >= 1e9 else minCoins

        dp = {}
        def dfs(cost):
            if(cost in dp):
                return dp[cost]
            if(cost == amount):
                return 0

            res = float("inf")
            for c in coins:
                if(c + cost <= amount):
                    res = min(res, 1 + dfs(cost + c))
            
            dp[cost] = res
            return res

        val = dfs(0)
        return -1 if val == float("inf") else val
        
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        dp = {}

        def dfs(num):
            if(num in dp):
                return dp[num]
            if(num == 0):
                return 1
            if(num == 1):
                return x
            if(num == -1):
                return 1/x
            
            val_1 = dfs(num % 2)

            val_2 = dfs(num // 2)
            # print(" the num: ", num, " and ", val_1, val_2)
            dp[num] = val_1 * (val_2 * val_2)
            return dp[num]
        
        return dfs(n)
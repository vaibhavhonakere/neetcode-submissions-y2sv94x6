class Solution:
    def numDecodings(self, s: str) -> int:
        # using ord to calculate the number
        dp = {}

        def dfs(i):
            if(i == len(s)):
                return 1
            if(i > len(s)):
                return 0
            if(i in dp):
                return dp[i]
            
            count_ways = 0
            for j in range(i, len(s)):
                if((j - i >= 1 and int(s[i:j + 1]) > 26) or 
                   (j - i >= 0 and s[i:j + 1][0] == "0")):
                    continue
                count_ways += dfs(j + 1)

            dp[i] = count_ways
            return dp[i]
        
        return dfs(0)

        
    
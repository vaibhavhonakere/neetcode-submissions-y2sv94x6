class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M = len(word1)
        N = len(word2)
        dp = [[float("inf") for j in range(N + 1)] for i in range(M + 1)]
        
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        dp[M][N] = 0

        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if(word1[i] == word2[j]):
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j + 1], dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]
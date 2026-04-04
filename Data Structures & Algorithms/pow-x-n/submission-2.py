class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def dfs(n):
            if(n == 0):
                return 1
            if(n == -1):
                return (1/x)
            if(n == 1):
                return x
            return dfs(n // 2) * dfs(n - (n // 2))
        
        return dfs(n)
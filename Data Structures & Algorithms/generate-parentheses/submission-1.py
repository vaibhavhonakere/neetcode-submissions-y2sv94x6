class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(openB, closedB, subset):
            if(closedB == n):
                res.append("".join(subset.copy()))
                return
            
            if(openB < n):
                subset.append("(")
                dfs(openB + 1, closedB, subset)
                subset.pop()
            if(closedB < openB):
                subset.append(")")
                dfs(openB, closedB + 1, subset)
                subset.pop()
        
        dfs(0,0,[])
        return res
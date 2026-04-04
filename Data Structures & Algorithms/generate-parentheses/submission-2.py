class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def backtrack(openB, closedB, subset):
            nonlocal ret
            if(openB == closedB == n):
                # print("".join(subset))
                ret.append("".join(subset))
                return
            
            if(openB < n):
                subset.append("(")
                print(subset)
                backtrack(openB + 1, closedB, subset)
                subset.pop()
            
            if(openB > closedB):
                subset.append(")")
                backtrack(openB, closedB + 1, subset)
                subset.pop()
        
        backtrack(0,0,[])
        return (ret)
        # return ret
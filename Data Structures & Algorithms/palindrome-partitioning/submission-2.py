class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        
        res = []
        def backtrack(i, subset):
            if(i >= len(s)):
               res.append(subset[::])
               return


            for j in range(i, len(s)):
                if(isPali(i, j)):
                    subset.append(s[i:j+1])
                    backtrack(j + 1, subset)
                    subset.pop()

        backtrack(0, [])
        return res
            

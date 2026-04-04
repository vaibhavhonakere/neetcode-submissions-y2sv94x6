class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        mapping = {i: 0 for i in range(1, n + 1)}

        # The town judge doesn't have an outgoing edge

        for x,y in trust:
            mapping[x] -= 1
            mapping[y] += 1
        
        for i in range(1, n + 1):
            if(mapping[i] == n - 1):
                return i
        
        return -1
        

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta = defaultdict(int)

        for s, d in trust:
            delta[s] -= 1
            delta[d] += 1
        
        for p in delta:
            if delta[p] == n - 1:
                return p
        
        return -1 

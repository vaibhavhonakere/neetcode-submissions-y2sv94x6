class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Calculate the in-degree and the out-degress of the
        # the trusted people
        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        for a, b in trust:
            indegree[b] += 1
            outdegree[a] += 1
        
        candidate = -1
        for judge in indegree:
            if(indegree[judge] == n - 1):
                candidate = judge
        
        if(candidate != -1 and outdegree[candidate] == 0):
            return candidate
        
        return -1

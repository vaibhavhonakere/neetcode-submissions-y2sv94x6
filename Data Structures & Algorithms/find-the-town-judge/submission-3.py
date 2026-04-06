class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Calculate the in-degree and the out-degress of the
        # the trusted people
        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        for x,y in trust:
            outdegree[x] += 1
            indegree[y] += 1
        
        
        possible_judge = None
        for person,count in indegree.items():
            if(count == n - 1):
                possible_judge = person
                break
        
        if(not(possible_judge) or outdegree[possible_judge] != 0):
            return -1
        
        return possible_judge

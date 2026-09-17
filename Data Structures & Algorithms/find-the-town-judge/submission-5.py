class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Calculate the in-degree and the out-degress of the
        # the trusted people
        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        for a,b in trust:
            indegree[a] += 1
            outdegree[b] += 1
        
        possible_ans = -1

        for judge in outdegree:
            if outdegree[judge] == n - 1:
                possible_ans = judge
                break
        
        # print(possible_ans, indegree[possible_ans])
        if(possible_ans == -1 or indegree[possible_ans] != 0):
            return -1
        
        return possible_ans

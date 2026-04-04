class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        preReqMap = {i: [] for i in range(numCourses)}
        sourceMap = {}

        def dfs(node):
            if(node not in sourceMap):
                sourceMap[node] = set()
                for prereq in preReqMap[node]:
                    sourceMap[node] |= dfs(prereq)
                sourceMap[node].add(node)
            return sourceMap[node]

        for x,y in prerequisites:
            preReqMap[y].append(x)
        
        for i in range(numCourses):
            dfs(i)
        
        res = []
        for (i,j) in queries:
            res.append(i in sourceMap[j])
        return res
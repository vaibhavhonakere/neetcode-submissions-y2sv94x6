class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        preReqMap = {i: [] for i in range(numCourses)}
        sourceMap = {}

        def dfs(node):
            if(node in sourceMap):
                return sourceMap[node]
            
            sourceMap[node] = set()
            for n in preReqMap[node]:
               sourceMap[node] |= dfs(n) 

            sourceMap[node].add(node)
            return sourceMap[node]
            

        for x,y in prerequisites:
            preReqMap[y].append(x)
        
        for i in range(numCourses):
            dfs(i)
        print(sourceMap)
        
        res = []
        for (i,j) in queries:
            res.append(i in sourceMap[j])
        return res
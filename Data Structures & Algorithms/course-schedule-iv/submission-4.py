class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjMap = {i: [] for i in range(numCourses)}

        for a,b in prerequisites:
            adjMap[b].append(a)

        def dfs(node):
            if(node in prereqMap):
                return prereqMap[node]

            prereqMap[node] = set()
            for nei in adjMap[node]:
                prereqMap[node] |= dfs(nei)
            
            prereqMap[node].add(node)
            return prereqMap[node]
        
        prereqMap = {}
        for crs in range(numCourses):
            dfs(crs)

        ret = []
        for u,v in queries:
            ret.append(u in prereqMap[v])
        return ret

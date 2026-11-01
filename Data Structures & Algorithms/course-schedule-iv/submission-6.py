class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjMap = {i: [] for i in range(numCourses)}

        for preq,course in prerequisites:
            adjMap[course].append(preq)

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

        return [u in prereqMap[v] for u,v in queries]

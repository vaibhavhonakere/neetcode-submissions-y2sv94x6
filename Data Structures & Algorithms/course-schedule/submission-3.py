class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjMap = {i: [] for i in range(numCourses)}

        for a,b in prerequisites:
            adjMap[a].append(b)
        
        visit = set()
        def dfs(node):
            if(node in visit):
                return False
            if(adjMap[node] == []):
                return True
            
            visit.add(node)
            for nei in adjMap[node]:
                if(not(dfs(nei))):
                    return False

            visit.remove(node)
            adjMap[node] = []
            return True
        
        for i in range(numCourses):
            if(not(dfs(i))):
                return False
        return True

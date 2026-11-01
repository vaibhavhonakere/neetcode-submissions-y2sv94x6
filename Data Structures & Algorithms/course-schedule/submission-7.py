class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build out indegree and outdegree nodes possibly

        indegree = defaultdict(int)
        adj_map = {i: [] for i in range(numCourses)}

        for src, preq in prerequisites:
            indegree[src] += 1
            adj_map[preq].append(src)
        
        queue = deque([])
        n = numCourses
        for i in range(numCourses):
            if(indegree[i] == 0):
                queue.append(i)
                n -= 1

        # print(queue)
        while(queue):
            node = queue.popleft()
            for nei in adj_map[node]:
                indegree[nei] -= 1
                if(indegree[nei] == 0):
                    queue.append(nei)
                    n -= 1
        
        return n == 0
        



        # adjMap = {i: [] for i in range(numCourses)}

        # for a,b in prerequisites:
        #     adjMap[a].append(b)
        
        # visit = set()
        # seen = set()
        # def dfs(node):
        #     if(node in visit):
        #         return False
        #     if(node in seen):
        #         return True

        #     visit.add(node)
        #     for nei in adjMap[node]:
        #         if(not(dfs(nei))):
        #             return False

        #     visit.remove(node)
        #     seen.add(node)
        #     return True
        
        # for i in range(numCourses):
        #     if(not(dfs(i))):
        #         return False
        # return True

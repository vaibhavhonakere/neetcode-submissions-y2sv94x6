class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjMap = {i: [] for i in range(n)}

        for src,dest in edges:
            adjMap[src].append(dest)
            adjMap[dest].append(src)
        
        visit = set()
        def dfs(node):
            if(node in visit):
                return
            
            visit.add(node)
            for nei in adjMap[node]:
                dfs(nei)
            
        count = 0
        for i in range(n):
            if(i not in visit):
                dfs(i)
                count += 1
        
        return count


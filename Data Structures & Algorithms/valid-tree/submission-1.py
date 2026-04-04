class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjMap = {i: [] for i in range(n)}

        for x,y in edges:
            adjMap[x].append(y)
            adjMap[y].append(x)
        
        visit = set()
        def dfs(node, prev):
            if(node in visit):
                return False
            
            visit.add(node)
            for n in adjMap[node]:
                if(n == prev):
                    continue
                if(not(dfs(n, node))):
                    return False
            
            return True

        if(not(dfs(0, -1))):
            return False
        return len(visit) == n

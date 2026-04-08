class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adjMap = {i:[] for i in range(n)}

        for src, dest in edges:
            adjMap[src].append(dest)
            adjMap[dest].append(src)
        
        visit = set()

        def dfs(node, prev):
            if(node in visit):
                return False
            
            visit.add(node)
            for nei in adjMap[node]:
                if(nei == prev):
                    continue
                if(not(dfs(nei, node))):
                    return False

            return True
            

        # print(visit)

        return len(visit) == n if dfs(0, -1) else False
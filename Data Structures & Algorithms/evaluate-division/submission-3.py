class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_map = defaultdict(list)  # mapping of a -> b, val and b -> a, 1 / val

        for (a,b), val in zip(equations, values):
            adj_map[a].append([b, val])
            adj_map[b].append([a, 1 / val])
        
        visit = set()

        def dfs(node, target, visit):
            if(node not in adj_map or target not in adj_map):
                return -1
            
            if(node == target):
                return 1
            
            visit.add(node)
            for nei, w in adj_map[node]:
                if(nei not in visit):
                    val = dfs(nei, target, visit)
                    if(val != -1):
                        return w * val
            
            return -1
        
        ret = []
        for u,v in queries:
            ret.append(dfs(u,v,set()))
        
        return ret

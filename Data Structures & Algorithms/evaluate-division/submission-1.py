class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjMap = defaultdict(list)
        for (x,y), v in zip(equations, values):
            adjMap[x].append((y, v))
            adjMap[y].append((x, 1 / v))
        
        def dfs(n, target, weight, visit):
            if(n not in adjMap):
                return -1
            if(n == target):
                return weight
            visit.add(n)
            for (nei, w) in adjMap[n]:
                if(nei in visit):
                    continue
                newWeight = weight * w
                val = dfs(nei, target, newWeight, visit)
                if(val != -1):
                    return val
            return -1   
        
        ret = []
        for i,j in queries:
            ret.append(dfs(i,j, 1, set()))
        return ret
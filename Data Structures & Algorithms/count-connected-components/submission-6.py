class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DFS Approach
        adjMap = defaultdict(list)
        visit = set()
        for x,y in edges:
            adjMap[x].append(y)
            adjMap[y].append(x)
        
        def dfs(node):
            if(node in visit):
                return
            visit.add(node)
            for n in adjMap[node]:
                dfs(n)
                    
        

        count = 0
        for i in range(n):
            if(i not in visit):
                dfs(i)
                count += 1
        
        return count





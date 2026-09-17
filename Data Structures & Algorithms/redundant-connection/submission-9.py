class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rank = [1]*(len(edges) + 1)
        par = [i for i in range(len(edges) + 1)]

        def find(n1):
            res = par[n1]
            while(res != par[res]):
                par[res] = par[par[res]]
                res = par[res]

            return res
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if(p1 == p2):
                return False

            if(rank[p1] < rank[p2]):
                rank[p2] += rank[p1]
                par[p1] = p2
            else:
                rank[p1] += rank[p2]
                par[p2] = p1
            
            return True
        
        for src, des in edges:
            if(not(union(src, des))):
                return [src, des]


        # n = len(edges)
        # adj = {i:[] for i in range(n + 1)}

        # def dfs(node, par):
        #     if node in visit:
        #         return True

        #     visit.add(node)
        #     for nei in adj[node]:
        #         if nei == par:
        #             continue
        #         if dfs(nei, node):
        #             return True
        #     return False

        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
        #     visit = set()

        #     if dfs(u, -1):
        #         return [u, v]
        # return []
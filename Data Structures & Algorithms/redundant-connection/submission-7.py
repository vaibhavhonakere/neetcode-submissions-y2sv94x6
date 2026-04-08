class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1]*(len(edges) + 1)

        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            par_1 = find(n1)
            par_2 = find(n2)

            if(par_1 == par_2):
                return False

            if(rank[par_1] > rank[par_2]):
                rank[par_1] += rank[par_2]
                par[par_2] = par_1
            else:
                rank[par_2] += rank[par_1]
                par[par_1] = par_2
            
            return True
        
        for a,b in edges:
            if(not(union(a,b))):
                return [a,b]
        
        return n
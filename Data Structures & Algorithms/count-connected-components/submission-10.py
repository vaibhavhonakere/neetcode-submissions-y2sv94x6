class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # adjMap = {i: [] for i in range(n)}

        # for src,dest in edges:
        #     adjMap[src].append(dest)
        #     adjMap[dest].append(src)
        
        # visit = set()
        # def dfs(node):
        #     if(node in visit):
        #         return
            
        #     visit.add(node)
        #     for nei in adjMap[node]:
        #         dfs(nei)
            
        # count = 0
        # for i in range(n):
        #     if(i not in visit):
        #         dfs(i)
        #         count += 1
        
        # return count

        # Union Find Algorithm
        par = [i for i in range(n)]
        rank = [1]*n

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
            if(union(a,b)):
                n -= 1
        
        return n
        








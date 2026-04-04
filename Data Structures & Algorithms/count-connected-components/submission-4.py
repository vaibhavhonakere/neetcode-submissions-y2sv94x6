class UnionFind:
    def __init__(self, n):
        self.parent =  [i for i in range(n)]
        self.rank = [1]*n
    
    def find(self, node):
        cur = node
        while(self.parent[cur] != cur):
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur
    
    def union(self, u, v):
        p1, p2 = self.find(u), self.find(v)
        if(p1 == p2):
            return False
        
        if(self.rank[p1] > self.rank[p2]):
            self.rank[p1] += self.rank[p2]
            self.parent[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.parent[p1] = p2
        return True 


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        disjointSet = UnionFind(n)
        count = 0
        for x,y in edges:
            if((disjointSet.union(x,y))):
                count += 1
        return n - count



        
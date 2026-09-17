class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjMap = {i:[] for i in range(n)}

        for src, dest in edges:
            adjMap[src].append(dest)
            adjMap[dest].append(src)
        
        min_height = n

        def dfs(node, prev, height):
            tmp = 0
            for nei in adjMap[node]:
                if(nei == prev):
                    continue
                tmp = max(tmp, 1 + dfs(nei, node, height))
            
            return tmp
        
        ret = []
        for i in range(n):
            min_dfs_height = dfs(i, -1, 0)
            if(min_height > min_dfs_height):
                min_height = min_dfs_height
                ret = [i]
            elif(min_height == min_dfs_height):
                ret.append(i)
            
        return ret
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjMap = {i:[] for i in range(n)}

        for src, dest in edges:
            adjMap[src].append(dest)
            adjMap[dest].append(src)
        
        # visit = set()
        min_height = n

        def dfs(node, prev, height):
            nonlocal min_dfs_height
            height = 0
            for nei in adjMap[node]:
                if(nei == prev):
                    continue
                height = max(height, 1 + dfs(nei, node, height))
            
            return height
        
        ret = []
        for i in range(n):
            min_dfs_height = dfs(i, -1, 0)
            if(min_height > min_dfs_height):
                min_height = min_dfs_height
                ret = [i]
            elif(min_height == min_dfs_height):
                ret.append(i)
            
        return ret
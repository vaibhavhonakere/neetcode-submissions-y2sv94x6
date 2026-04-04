"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, i, j):
            allSame = True
            for r in range(n):
                for c in range(n):
                    if(grid[i][j] != grid[i + r][j + c]):
                        allSame = False
                        break
            
            if(allSame):
                return Node(grid[i][j], True)
            n = n // 2
            topLeft = dfs(n, i, j)
            topRight = dfs(n, i, j + n)
            botLeft = dfs(n, i + n, j)
            botRight = dfs(n, i + n, j + n)

            return Node(0, False, topLeft, topRight, botLeft, botRight)
        
        return dfs(len(grid), 0, 0)
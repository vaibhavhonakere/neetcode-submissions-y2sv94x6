"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copy = {None: None}

        def dfs(n):
            if(n in copy):
                return copy[n]
            copy_node = Node(n.val)
            copy[n] = copy_node
            for nei in n.neighbors:
                copy[n].neighbors.append(dfs(nei))
            return copy[n]

        return dfs(node)
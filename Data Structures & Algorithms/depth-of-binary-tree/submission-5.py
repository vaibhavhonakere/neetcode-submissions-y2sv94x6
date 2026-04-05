# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = float("-inf")

        if(not(root)):
            return 0

        def dfs(node, lvl):
            nonlocal max_depth
            if(not(node)):
                return 0
            
            max_depth = max(max_depth, lvl)
            dfs(node.left, lvl + 1)
            dfs(node.right, lvl + 1)
            

        dfs(root, 1)
        return max_depth

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, prev):
            nonlocal count
            if(not(node)):
                return None
            
            if(prev <= node.val):
                count += 1
            
            dfs(node.left, max(prev, node.val))
            dfs(node.right, max(prev, node.val))
        
        dfs(root, -10000)
        return count
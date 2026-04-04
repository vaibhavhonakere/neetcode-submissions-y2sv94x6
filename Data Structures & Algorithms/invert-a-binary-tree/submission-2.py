# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if(not(node)):
                return None
            
            newNode = TreeNode(node.val)
            newNode.left = dfs(node.right)
            newNode.right = dfs(node.left)
            return newNode
        
        return dfs(root)
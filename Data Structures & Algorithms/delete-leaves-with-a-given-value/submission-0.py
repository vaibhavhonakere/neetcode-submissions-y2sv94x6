# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(node):
            if(not(node)):
                return None
            
            root = TreeNode(node.val)
            root.left = dfs(node.left)
            root.right = dfs(node.right)

            if(root.val == target and not(root.left) and not(root.right)):
                return None
            
            return root
        
        return dfs(root)
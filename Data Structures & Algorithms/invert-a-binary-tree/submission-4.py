# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if(not(root)):
                return None
            
            node = TreeNode(root.val)
            node.left = dfs(root.right)
            node.right = dfs(root.left)
            return node
        return dfs(root)
        # def dfs(node):
        #     if(not(node)):
        #         return None
            
        #     new_node = TreeNode(node.val)
        #     new_node.left = dfs(node.right)
        #     new_node.right = dfs(node.left)
        #     return new_node
        
        # return dfs(root)
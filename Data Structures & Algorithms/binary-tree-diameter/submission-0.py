# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDepth = [0]
        def dfs(node):
            if(not(node)):
                return 0
            
            depth_1 = dfs(node.left)
            depth_2 = dfs(node.right)
            if(depth_1 + depth_2 > maxDepth[0]):
                maxDepth[0] = depth_1 + depth_2
            return max(depth_1, depth_2) + 1
        dfs(root)
        return maxDepth[0]
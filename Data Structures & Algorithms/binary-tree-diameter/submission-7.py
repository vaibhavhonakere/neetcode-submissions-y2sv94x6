# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest_diameter = -1
        def dfs(node):
            nonlocal longest_diameter

            if(not(node)):
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if(left + right > longest_diameter):
                longest_diameter = max(longest_diameter, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return longest_diameter
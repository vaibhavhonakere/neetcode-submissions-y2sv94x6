# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if(not(root)):
            return True
        max_diameter = True
        def dfs(node):
            nonlocal max_diameter
            if(not(node)):
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            if(abs(right - left) > 1):
                max_diameter = False
            return 1 + max(left, right)

        dfs(root)
        return max_diameter
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float("-inf")

        def dfs(node):
            nonlocal max_path
            if(not(node)):
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            curMaxLeft = max(left, 0)
            curMaxRight = max(right, 0)

            max_path = max(max_path, node.val + curMaxLeft + curMaxRight)

            return node.val + max(curMaxLeft, curMaxRight)
        
        dfs(root)
        return max_path
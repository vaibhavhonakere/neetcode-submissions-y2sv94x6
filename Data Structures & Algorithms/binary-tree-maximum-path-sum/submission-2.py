# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxVal = [float("-inf")]
        def dfs(root):
            if(not(root)):
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            left = max(left, 0)
            right = max(right, 0)
            if(left + right + root.val > maxVal[0]):
                maxVal[0] = left + right + root.val
            return max(left, right) + root.val
        dfs(root)
        return maxVal[0]

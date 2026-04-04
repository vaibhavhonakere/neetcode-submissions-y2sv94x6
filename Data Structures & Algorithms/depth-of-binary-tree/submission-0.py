# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxVal = [0]
        def dfs(node, count):
            if(not(node)):
                return None
            maxVal[0] = max(maxVal[0], count)
            dfs(node.left, count + 1)
            dfs(node.right, count + 1)

        dfs(root, 1)
        return maxVal[0]

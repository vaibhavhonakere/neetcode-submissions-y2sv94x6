# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = float("-inf")
        def dfs(node):
            nonlocal maxPath
            if(not(node)):
                return 0
            
            curLeft = dfs(node.left)
            curRight = dfs(node.right)
            if(curRight < 0):
                curRight = 0
            if(curLeft < 0):
                curLeft = 0
            
            if(node.val + curRight + curLeft > maxPath):
                maxPath = max(maxPath, node.val + curRight + curLeft)

            return max(curLeft, curRight) + node.val
        
        dfs(root)
        return maxPath
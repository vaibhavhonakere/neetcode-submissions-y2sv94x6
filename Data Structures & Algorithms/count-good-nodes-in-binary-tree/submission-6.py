# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, check):
            nonlocal count
            if(not(node)):
                return None
            
            print(node.val, check)
            if(node.val >= check):
                check = node.val
                count += 1
            
            dfs(node.left, check)
            dfs(node.right, check)
        
        dfs(root, root.val)
        return count
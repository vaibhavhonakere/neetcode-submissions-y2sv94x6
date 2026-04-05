# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if(not(root)):
            return 0
        
        count_of_good_nodes = 0

        def dfs(node, prev_max):
            nonlocal count_of_good_nodes
            if(not(node)):
                return None
            
            if(node.val >= prev_max):
                count_of_good_nodes += 1
                prev_max = max(prev_max, node.val)
            
            dfs(node.left, prev_max)
            dfs(node.right, prev_max)
        
        dfs(root, root.val)
        return count_of_good_nodes

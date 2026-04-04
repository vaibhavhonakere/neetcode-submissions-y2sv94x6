# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if(not(p) and not(q)):
                return True
            
            if(not(p) or not(q)):
                return False
            
            if(p and q and p.val != q.val):
                return False
            
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        def dfs(root, subTree):
            if(not(subTree)):
                return True
            if(not(root)):
                return False
            if(isSameTree(root, subTree)):
                return True
            
            return dfs(root.left, subTree) or dfs(root.right, subTree)
        
        return dfs(root,subRoot)



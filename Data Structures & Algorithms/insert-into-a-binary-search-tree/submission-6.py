# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if(not(root)):
            return TreeNode(val)
        curr = root
        while(root):
            if(root.val > val):
                if(not(root.left)):
                    root.left = TreeNode(val)
                root = root.left
            elif(root.val < val):
                if(not(root.right)):
                    root.right = TreeNode(val)
                root = root.right
            else:
                break
        
        return curr
